
$(document).on('ready', main_sales );

//GLOBAL SELECTORS
//------------------------------------------------------------------------------------------
var product_panel = $('.cd-panel-search-product');
var client_panel = $('.cd-panel-search-client');
var pay_panel = $('.cd-panel-pay');

var btn_product_search = $('.product-search-btn');
var btn_client_search = $('.btn-client-search');
var btn_pay = $('.btn-pay');
//------------------------------------------------------------------------------------------

//MAIN
//------------------------------------------------------------------------------------------
function main_sales() {

    //EVENTS
    browser_object_events();

    //LOAD TO LOCAL STORAGE
    load_to_local_storage();

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
function load_to_local_storage(){

    localStorage.Products=null;
    localStorage.Clients=null;
    products_to_memory();
    clients_to_memory();
}

function products_to_memory() {

    $.get('/api/products/', function (data) {

        localStorage.Products=JSON.stringify(data);
    });

}//SAVE PRODUCTS TO LOCAL STORAGE

function clients_to_memory() {

    $.get('/api/clients/', function (data) {

        localStorage.Clients=JSON.stringify(data);
    });

}//SAVE CLIENTS TO LOCAL STORAGE
//------------------------------------------------------------------------------------------

//BROWSER EVENTS FUNCTION
//------------------------------------------------------------------------------------------
function browser_object_events(){

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

}// BROWSER EVENTS ENDS
//------------------------------------------------------------------------------------------