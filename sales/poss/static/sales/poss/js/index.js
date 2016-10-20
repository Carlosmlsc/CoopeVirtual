
$(document).on('ready', mainSales );

//GLOBAL VARS
//------------------------------------------------------------------------------------------
var saleList = [];
//------------------------------------------------------------------------------------------

//GLOBAL SELECTORS
//------------------------------------------------------------------------------------------
var product_panel = $('.cd-panel-search-product');
var client_panel = $('.cd-panel-search-client');
var pay_panel = $('.cd-panel-pay');

var btn_product_search = $('.product-search-btn');
var btn_client_search = $('.btn-client-search');
var btn_pay = $('.btn-pay');

var product_code_field = $('.product_code_field');

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

}//main
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
}

function productsToMemory() {

    $.get('/api/products/', function (data) {

        localStorage.Products=JSON.stringify(data);
    });

}//SAVE PRODUCTS TO LOCAL STORAGE

function clientsToMemory() {

    $.get('/api/clients/', function (data) {

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

    var pudisc = (products[0].price)*((100-products[0].discount)/100);

    var iv=0;

    if( products[0].usetaxes){
        iv=products[0].taxes;
    }

    addNewRow(products[0].code, products[0].barcode, products[0].description, qty, products[0].price , subt,
                      products[0].id, products[0].discount, iv, pudisc);


}

function addNewRow(code, barcode, desc, qty, uprice, subt, id, disc, iv, pudisc){

    saleList.push([code, barcode, qty, parseFloat(uprice), subt, desc, id, disc, iv]);
    // code, barcode, qty, unit price, subt, discount %, id, iv,

    var newRow=`<tr class="${code}">
                    <td>${code}</td>
                    <td>${desc}</td>
                    <td style="padding:0; width:8%"><input type="number" style="width:100%;border:0px" 
                    class="form-control ${code}_product_qty product_qty"/></td>
                    <td class="${code}_product_uprice price" >${parseFloat(uprice).toFixed(2)}</td>
                    <td style="padding:0; width:7%"><input value="${disc}" type="number" style="width:100%;border:0px" 
                    class="form-control ${code}_product_disc no_disc"/></td>
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

    // code, barcode, qty, unit price, subt, discount %, id, iv,
    $.each(saleList, function(i) {

        subtotal = subtotal+saleList[i][4];//new_order_array[i][3] is the subt amount.
        iv_amount=iv_amount+(saleList[i][4]*(saleList[i][8]/100));//saleList[i][8] is the IV


    });

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

function searchProduct(text){

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
            addToSearhTable(products[i]);
        }

    });


}

function addToSearhTable(product){

    

}

function rowUpdate(row, code, qty, array, ctrl, disc){

    var actual_qty = 0;
    var actual_uprice = 0;
    var new_qty = 0;
    var new_subt = 0;
    var new_disc = 0;
    var new_pudisc = 0;


    if (ctrl == 1){//means add already existing product on table

        actual_qty = array[row][2];
        actual_uprice = array[row][3];
        new_disc =  array[row][7];

        new_qty = parseFloat(actual_qty) + parseFloat(qty);

        new_subt = (actual_uprice*new_qty)*(1-(new_disc/100));

        new_pudisc = (actual_uprice)*(1-(new_disc/100));

    }

    if(ctrl == 2){//means update qty

        actual_uprice = array[row][3];
        new_disc =  array[row][7];

        new_qty = parseFloat(qty);

        new_subt = (actual_uprice*new_qty)*(1-(new_disc/100));

        new_pudisc = (actual_uprice)*(1-(new_disc/100));

    }


    if(ctrl == 4){//means update discount

        actual_uprice = array[row][2];

        new_qty = array[row][1];

        new_disc =  disc;

        new_subt = (actual_uprice*new_qty)*(1-(new_disc/100));

        new_pudisc = (actual_uprice)*(1-(new_disc/100));
    }
    //calculate values


    //update values

    $(`.${code}_product_qty`).val(new_qty);
    $(`.${code}_product_subt`).text(new_subt.toFixed(2));

    array[row][2] = new_qty;
    array[row][3] = actual_uprice ;
    array[row][4] = new_subt;
    array[row][7] = new_disc;


    return array;

}
//------------------------------------------------------------------------------------------

//BROWSER EVENTS FUNCTIONS
//------------------------------------------------------------------------------------------
function browserObjectEvents(){

    //EVENTS PRODUCT SEARCH PANEL

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

    //EVENTS CLIENT SEARCH PANEL

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

    //EVENTS PAY PANEL

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

    //EVENTS PRODUCT CODE

    product_code_field.on('keypress', function (e) {
         if(e.which === 13){
             handleCode(product_code_field.val());
         }
    });

    // EVENTS SEARCH PRODUCT

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


}// BROWSER EVENTS ENDS
//------------------------------------------------------------------------------------------