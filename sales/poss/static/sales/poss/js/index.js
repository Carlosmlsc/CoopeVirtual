
$(document).on('ready', mainSales );

//GLOBAL VARS
//------------------------------------------------------------------------------------------
var saleList = [];
const companyId = $('#company-id').html();
//------------------------------------------------------------------------------------------

//GLOBAL SELECTORS
//------------------------------------------------------------------------------------------
var html = $('html');
var product_panel = $('.cd-panel-search-product');
var client_panel = $('.cd-panel-search-client');
var pay_panel = $('.cd-panel-pay');

var btn_product_search = $('.product-search-btn');
var btn_client_search = $('.btn-client-search');
var btn_pay = $('.btn-pay');

var product_code_field = $('.product_code_field');
var client_code_field = $('.client_code_field');

var total = 0;
var subtotal = 0;
var iv_amount = 0 ;
//------------------------------------------------------------------------------------------

//MAIN
//------------------------------------------------------------------------------------------
function mainSales() {

    //EVENTS
    browserObjectEvents();

    //LOAD TO LOCAL STORAGE
    loadToLocalStorage();

}//MAIN FUNCTION
//------------------------------------------------------------------------------------------

//UTIL FUNCTIONS
//------------------------------------------------------------------------------------------
function blurElement(element, size){

    var filterVal = 'blur('+size+'px)';
    $(element)
      .css('filter',filterVal)
      .css('webkitFilter',filterVal)
      .css('mozFilter',filterVal)
      .css('oFilter',filterVal)
      .css('msFilter',filterVal);

}
//------------------------------------------------------------------------------------------

//LOCAL STORAGE FUNCTIONS
//------------------------------------------------------------------------------------------
function loadToLocalStorage(){

    localStorage.Products=null;
    localStorage.Clients=null;
    productsToMemory();
    clientsToMemory();

}//MAIN SAVE TO LOCAL STORAGE

function productsToMemory() {

    $.get(`/api/products/?company=${companyId}`, function (data) {

        localStorage.Products=JSON.stringify(data);
    });

}//SAVE PRODUCTS TO LOCAL STORAGE

function clientsToMemory() {

    $.get(`/api/clients/?company=${companyId}`, function (data) {

        localStorage.Clients=JSON.stringify(data);
    });

}//SAVE CLIENTS TO LOCAL STORAGE
//------------------------------------------------------------------------------------------

//ACTION FUNCTIONS FUNCTIONS
//------------------------------------------------------------------------------------------
function handleCode(codeStr) {

    var products = JSON.parse(localStorage.Products);

    var code = codeStr.split('*')[0];
    var qty = codeStr.split('*')[1];

    if( qty === 0){
        alertify.alert('Error','La Cantidad no puede ser Cero');
        return false;
    }

    if( qty === undefined){
        qty=1;
    }

    var isOnArray = isCodeOnArray(saleList,code);

    if(isOnArray === -1){
        //filter product by code
        products = $.grep(products, function(element){
            return element.code == code;
        });

        if (products.length){

           prepareNewRow(products, qty);

        }
        else{
            products = $.grep(products, function(element){
                return element.barcode == code;
            });

            if (products.length){
                prepareNewRow(products, qty);
            }
            else{
                alertify.alert('Error','No existe un producto con el código seleccionado.')
            }
        }
    }//if

    else{

        saleList = rowUpdate(isOnArray, code, qty, saleList, 1,0);
        updateTotals();

    }//else


}

function isCodeOnArray(array , code){

    var control = -1;

    $.each(array, function(i) {

        if (array[i][0]==code || array[i][1]==code){ // Eval Code and Barcode
            control = i;
            return false;
        }
    });

    return control;
} //IS ON ARRAY FUNCTION

function prepareNewRow(products, qty) {

    var subt = (products[0].price*qty)*((100-products[0].discount)/100);

    var iv=0;

    if( products[0].usetaxes){
        iv=products[0].taxes;
    }

    addNewRow(products[0].code, products[0].barcode, products[0].description, qty, products[0].price , subt,
                      products[0].id, products[0].discount, iv);


}

function addNewRow(code, barcode, desc, qty, uprice, subt, id, disc, iv){

    saleList.push([code, barcode, qty, parseFloat(uprice), subt, desc, id, disc, iv]);
    // code, barcode, qty, unit price, subt, discount %, id, iv,

    var newRow=`<tr class="${code} product_row">
                    <td>${code}</td>
                    <td>${desc}</td>
                    <td style="padding:0; width:10%"><input type="number" style="width:100%;border:0px; padding: 0; text-align: center" 
                    class="form-control ${code}_product_qty product_qty"/></td>
                    <td class="${code}_product_uprice price" >${parseFloat(uprice).toFixed(2)}</td>
                    <td style="padding:0; width:10%"><input value="${disc}" type="number" style="width:100%;border:0px; padding:0;text-align: center" 
                    class="form-control ${code}_product_disc product_disc"/></td>
                    <td class="${code}_product_iv" >${iv}%</td>
                    <td class="${code}_product_subt price" >${subt.toFixed(2)}</td>
                    <td style="text-align: center; padding:0; width:5%" class="inner-addon">
                    <i class="fa fa-minus remove_row"></i></td>
                </tr>`;

    $('.table-body').append(newRow);

    $(`.${code}_product_qty`).val(qty);

    updateTotals();
}

function updateTotals() {

    subtotal=0;
    iv_amount= 0;
    var generalDiscount ;

    if ($('.sale_global_discount_input').val()){

        generalDiscount = parseFloat($('.sale_global_discount_input').val());

    }
    else{
        generalDiscount = 0;
    }


    // code, barcode, qty, unit price, subt, discount %, id, iv,
    $.each(saleList, function(i) {

        subtotal = subtotal+saleList[i][4];//saleList[i][4] is the subt amount.
        iv_amount=iv_amount+(saleList[i][4]*(saleList[i][8]/100));//saleList[i][8] is the IV


    });

    subtotal = subtotal*(1-(generalDiscount/100));
    iv_amount=iv_amount*(1-(generalDiscount/100));

    total = subtotal+iv_amount;

    iv_amount = parseFloat(iv_amount).toFixed(2);
    subtotal = parseFloat(subtotal).toFixed(2);
    total = total.toFixed(2);

    $('.sale_subtotal').text(subtotal);
    $('.sale_iv_amount').text(iv_amount);
    $('.sale_total').text(total);

    $('.product_code_field').val('');


    $('.price').priceFormat({
        prefix: '₡ ',
        centsSeparator: ',',
        thousandsSeparator: '.'
    });
}

function rowUpdate(row, code, qty, array, ctrl, disc){

    var actualQty = 0;
    var actualUprice = 0;
    var newQty = 0;
    var newSubt = 0;
    var newDisc = 0;

    if (ctrl == 1){//means add already existing product on table

        actualQty = array[row][2];
        actualUprice = array[row][3];
        newDisc =  array[row][7];

        newQty = parseFloat(actualQty) + parseFloat(qty);

        newSubt = (actualUprice*newQty)*(1-(newDisc/100));


    }

    if(ctrl == 2){//means update qty



        actualUprice = array[row][3];
        newDisc =  array[row][7];

        newQty = parseFloat(qty);

        newSubt = (actualUprice*newQty)*(1-(newDisc/100));

    }

    if(ctrl == 4){//means update discount

        actualUprice = array[row][3];

        newQty = array[row][2];

        newDisc =  disc;

        newSubt = (actualUprice*newQty)*(1-(newDisc/100));

    }

    if(newQty <= 0){

        alertify.alert('Error', 'La cantidad no puede ser cero, ni menor a cero, el valor volverá a 1');

        rowUpdate(row, code, 1, saleList, 2,0);

        updateTotals();

        return array;

    }

    //update values

    $(`.${code}_product_qty`).val(newQty);
    $(`.${code}_product_subt`).text(newSubt.toFixed(2));

    array[row][2] = newQty;
    array[row][4] = newSubt;
    array[row][7] = newDisc;

    return array;

}

function searchProduct(text){

    $('.table-body-product-search').html('');

    var products = JSON.parse(localStorage.Products);
    var description;

    text = text.split('%');

    $.each(products, function(i) {

        description = products[i].description.toString();
        var control = true;

        $.each(text, function(i) {

        var index = description.toLowerCase().indexOf(text[i].toLowerCase());

        if (index == -1){
            control = false;
            return false;
        }

        });

        if (control == true){
            addToSearchProductTable(products[i]);
        }

    });



}

function addToSearchProductTable(product){

    var code  = product.code;
    var desc = product.description;
    var price = parseFloat(product.sellprice).toFixed(2);
    var inventory;


    if(product.useinventory){
        inventory = product.inventory;
    }
    else{
        inventory = '-';
    }

    var newRow=`<tr class="${code}">
                    <td>${code}</td>
                    <td>${desc}</td>
                    <td>${inventory}</td>
                    <td class="price">${price}</td>
                    <td style="text-align: center; padding:0; width:5%" class="inner-addon">
                    <i class="fa fa-plus select_product_search_row"></i></td>
                </tr>`;

    $('.table-body-product-search').append(newRow);

     $('.price').priceFormat({
        prefix: '₡ ',
        centsSeparator: ',',
        thousandsSeparator: '.'
    });


}

function searchClient(text){

    $('.client-search-table-body').html('');

    var clients = JSON.parse(localStorage.Clients);
    var name;

    text = text.split('%');

    $.each(clients, function(i) {

        name = clients[i].name.toString() + ' ' +clients[i].last_name.toString();
        var control = true;

        $.each(text, function(i) {

        var index = name.toLowerCase().indexOf(text[i].toLowerCase());

        if (index == -1){
            control = false;
            return false;
        }

        });

        if (control == true){
            addToSearchClientTable(clients[i]);
        }

    });

}

function addToSearchClientTable(client){

    var code  = client.code;
    var name = client.name.toString() + ' ' +client.last_name.toString();
    var hasCredit;
    var debt = parseFloat(client.debt).toFixed(2);



    if(client.has_credit){
        hasCredit = 'fa fa-check';
    }
    else{
        hasCredit = 'fa fa-minus';
    }

    var newRow=`<tr class="${code}">
                    <td>${code}</td>
                    <td>${name}</td>
                    <td><i class="${hasCredit}"></i></td>
                    <td class="price">${debt}</td>
                    <td style="text-align: center; padding:0; width:5%" class="inner-addon">
                    <i class="fa fa-plus select_client_search_row"></i></td>
                </tr>`;

    $('.client-search-table-body').append(newRow);

     $('.price').priceFormat({
        prefix: '₡ ',
        centsSeparator: ',',
        thousandsSeparator: '.'
    });


}

function setClient(code){

    var clients = JSON.parse(localStorage.Clients);
    var control = -1;
    var name;
    var hasCredit;
    var debt;

    $.each(clients, function(i) {

        if(code == clients[i].code.toLowerCase()){
            control=i;
            return false
        }

    });

    if (control != -1){

        name = clients[control].name.toString() + ' ' +clients[control].last_name.toString();
        hasCredit = clients[control].has_credit;
        debt = clients[control].debt;

        $('.client-name-span').html(name);

        if(hasCredit){
            $('.client-credit-span').removeClass('fa-times-circle');
            $('.client-credit-span').addClass('fa-check-square');
        }
        else{
            $('.client-credit-span').removeClass('fa-check-square');
            $('.client-credit-span').addClass('fa-times-circle');
        }

        $('.debt-amount-span').html(parseFloat(debt).toFixed(2));
        $('.debt-amount-span').addClass('credit-negative')



    }
    else{
        $('.client-name-span').html('Cliente de Contado');

        $('.client-credit-span').removeClass('fa-check-square');
        $('.client-credit-span').addClass('fa-times-circle');

        $('.debt-amount-span').html('-');

        alertify.alert('Error', 'No existe un cliente con ese código');
    }






}

//------------------------------------------------------------------------------------------
//BROWSER EVENTS FUNCTIONS
//------------------------------------------------------------------------------------------
function browserObjectEvents(){

    //EVENTS PRODUCT SEARCH PANEL
    //--------------------------------------------------------------------------------------

    btn_product_search.on('click', function(event){
        event.preventDefault();
        product_panel.addClass('is-visible');
        blurElement('.blur-div',2);

    });

    product_panel.on('click', function(event){
        if( $(event.target).is('.cd-panel') || $(event.target).is('.cd-panel-close') ) {
            product_panel.removeClass('is-visible');
            blurElement('.blur-div',0);
            event.preventDefault();
        }
    });

    $('#btncerrarbuscar').on('click', function(event){
            product_panel.removeClass('is-visible');
            blurElement('.blur-div',0);
            event.preventDefault();
    });

    //---------------------------------------------------------------------------------------

    //EVENTS CLIENT SEARCH PANEL
    //---------------------------------------------------------------------------------------

    btn_client_search.on('click', function(event){
        event.preventDefault();
        client_panel.addClass('is-visible');
        blurElement('.blur-div',2);
    });

    client_panel.on('click', function(event){
        if( $(event.target).is('.cd-panel') || $(event.target).is('.cd-panel-close') ) {
            client_panel.removeClass('is-visible');
            blurElement('.blur-div',0);
            event.preventDefault();
        }
    });

    $('#btncerrarbuscarcliente').on('click', function(event){
            client_panel.removeClass('is-visible');
            blurElement('.blur-div',0);
            event.preventDefault();
    });
    //---------------------------------------------------------------------------------------

    //EVENTS PAY PANEL
    //---------------------------------------------------------------------------------------

    btn_pay.on('click', function(event){
        event.preventDefault();
        pay_panel.addClass('is-visible');
        blurElement('.blur-div',2);
    });

    pay_panel.on('click', function(event){
        if( $(event.target).is('.cd-panel') || $(event.target).is('.cd-panel-close') ) {
            pay_panel.removeClass('is-visible');
            blurElement('.blur-div',0);
            event.preventDefault();
        }
    });

    $('#btncerrarbuscarpay').on('click', function(event){
            pay_panel.removeClass('is-visible');
            blurElement('.blur-div',0);
            event.preventDefault();
    });
    //---------------------------------------------------------------------------------------

    //EVENTS PRODUCT CODE

    product_code_field.on('keypress', function (e) {
         if(e.which === 13){
             handleCode(product_code_field.val());
         }
    });

    // EVENTS PRODUCT SEARCH ACTIONS
    //---------------------------------------------------------------------------------------

    $('#btnbusqueda').on('click', function(event){

        event.preventDefault();
        searchProduct($('#busqueda').val());

    });

    $('#busqueda').on('keypress', function (e) {

        if(e.which === 13){
            e.preventDefault();
            searchProduct($('#busqueda').val());
        }



    });

    html.on('click','.select_product_search_row', function (){

        event.preventDefault();

        var row=$(this).closest("tr");

        var productId = row.attr('class');

        product_code_field.val(productId);

        product_panel.removeClass('is-visible');

        blurElement('.blur-div',0);

        $('.table-body-product-search').html('');

        $('#busqueda').val('');

        product_code_field.focus();

    });
    //---------------------------------------------------------------------------------------

    // EVENTS CLIENT SEARCH ACTIONS
    //---------------------------------------------------------------------------------------

    $('#client-search-btn').on('click', function(event){

        event.preventDefault();
        searchClient($('#client-search-input').val());

    });

    $('#client-search-input').on('keypress', function (e) {

        if(e.which === 13){
            e.preventDefault();
            searchClient($('#client-search-input').val());
        }

    });

    html.on('click','.select_client_search_row', function (){

        event.preventDefault();

        var row=$(this).closest("tr");

        var clientCode = row.attr('class');

        client_code_field.val(clientCode);

        client_panel.removeClass('is-visible');

        blurElement('.blur-div',0);

        $('.client-search-table-body').html('');

        $('#client-search-input').val('');

        client_code_field.trigger('change');

        product_code_field.focus();

    });

    html.on('change','.client_code_field', function () {

        setClient(client_code_field.val());

    });

    //---------------------------------------------------------------------------------------
    html.on('change','.product_qty', function () {

        event.preventDefault();
        var row = $(this).closest("tr");
        var rowIndex = row.index();

        var code = saleList[rowIndex][0];
        var qty = $(`.${code}_product_qty`).val();
        var disc = saleList[rowIndex][5];

        rowUpdate(rowIndex, code, qty, saleList, 2,disc);

        updateTotals();

    });

    html.on('change','.product_disc', function () {

        event.preventDefault();
        let row = $(this).closest("tr");
        let rowIndex = row.index();

        var code = saleList[rowIndex][0];
        var qty = saleList[rowIndex][2];
        var disc = $(`.${code}_product_disc`).val();

        rowUpdate(rowIndex, code, qty, saleList, 4, disc);

        updateTotals();

    });

     html.on('change','.sale_global_discount_input', function () {
         console.log('entro');
         updateTotals();
     });


    html.on('click','.remove_row', function () {

        event.preventDefault();
        var row=$(this).closest("tr");
        var rowIndex = row.index();

        saleList.splice( rowIndex,1 );

        $(this).parent().parent().remove();

        updateTotals();

        if (saleList.length==0){

        }

    });

    //---------------------------------------------------------------------------------------


    // MOUSETRAP SHORTCUTS
    //---------------------------------------------------------------------------------------

    Mousetrap.bind('mod p', function (e) {
        e.preventDefault();
        product_panel.addClass('is-visible');
        blurElement('.blur-div',2);
    });

    Mousetrap.bind('mod c', function (e) {
        e.preventDefault();
        client_panel.addClass('is-visible');
        blurElement('.blur-div',2);
    });
    //---------------------------------------------------------------------------------------

    // KEYBOARD SHORTCUTS
    //---------------------------------------------------------------------------------------

    html.on('click','.product_row', function (){
        $('.table-product-selected').removeClass('table-product-selected');
        $(this).addClass("table-product-selected");
    });

    $(document).on('keydown', function (e) {

        var row=$('.table-product-selected');
        var rowIndex = row.index();
        var code;

        if(e.which == 46){//MEAN DELETE KEY

            if(rowIndex != -1){
                saleList.splice( rowIndex,1 );

                row.remove();

                updateTotals();

                if (saleList.length==0){

                }
            }

        }

        if(e.which == 107){//MEAN PLUS KEY

            if(rowIndex != -1){

                code = row.attr('class').split(' ')[0];

                rowUpdate(rowIndex, code, 1, saleList, 1,0);

                updateTotals();

            }

        }

        if(e.which == 109){//MEAN PLUS KEY

            if(rowIndex != -1){

                code = row.attr('class').split(' ')[0];

                rowUpdate(rowIndex, code, -1, saleList, 1,0);

                updateTotals();

            }

        }

    });

    $(':input').focusin(function () {///ON ANY INPUT FOCUS DESELECT ALL ROWS
        $('.table-product-selected').removeClass('table-product-selected');
    })


}// BROWSER EVENTS ENDS
//------------------------------------------------------------------------------------------