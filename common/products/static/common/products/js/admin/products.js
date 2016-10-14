/**
 * Created by emanuelziga on 17/6/16.
 */
(function($) {

    $(document).ready(function($) {

// SELECTORS

    var sell_price = $('#id_product_sellprice');
    var label_sell_price = $('.field-product_sellprice label');


    var use_inv = $('#id_product_useinventory');
    var div_inventory = $('.field-product_inventory');
    var div_min_inventory = $('.field-product_minimum');

    var autoprice = $('#id_product_autoprice');
    var div_utility = $('.field-product_utility');
    var div_price = $('.field-product_price');

    var use_taxes = $('#id_product_usetaxes');
    var div_taxes = $('.field-product_taxes');

    var taxes = $('#id_product_taxes');
    var cost = $('#id_product_cost');
    var utility = $('#id_product_utility');
    var price = $('#id_product_price');

    var btn_save = $("[name='_save']");


//SELECTORS END

    label_sell_price.css({"font-size": "16px"});
    sell_price.css({"font-size": "16px"});

    sell_price.prop('disabled', true);

    btn_save.on('click', function () {
        sell_price.prop('disabled', false);
    });

// FIELDS HIDE AND SHOW

//USE INVENTORY FIELDS
    if(use_inv.is(':checked')==false){

        div_inventory.hide();
        div_min_inventory.hide();
    }

    use_inv.change(function() {//USE INVENTORY TOGGLE

        if(use_inv.is(':checked')){
            div_inventory.show();
            div_min_inventory.show();
        }
        else {
            div_inventory.hide();
            div_min_inventory.hide();
        }

    });//USE INVENTORY ENDS

//AUTO PRICE FIELDS
    if(autoprice.is(':checked')==false){

        div_utility.hide();
        div_price.show();
    }
    else{
        div_utility.show();
        div_price.hide();
    }

    autoprice.change(function() {//AUTO PRICE TOGGLE

        if(autoprice.is(':checked')){
            div_utility.show();
            div_price.hide();
        }
        else {
            div_utility.hide();
            div_price.show();
        }

        SetSellPrice();
    });// AUTO PRICE TOGGLE ENDS

//USE TAXES FIELDS
    if(use_taxes.is(':checked')==false){

        div_taxes.hide();

    }
    use_taxes.change(function() {//USE TAXES TOGGLE

        if(use_taxes.is(':checked')){
            div_taxes.show();
        }
        else {
            div_taxes.hide();
        }

        SetSellPrice();

    });// USE TAXES TOGGLE ENDS

    taxes.change(function(){//TAXES FIELD CHANGES
        if (taxes.val()==""){
            taxes.val(parseFloat(0).toFixed(2));
        }
        SetSellPrice();
    });//ENDS TAXES FIELD CHANGES

    cost.change(function(){//COST FIELD CHANGES
        if (cost.val()==""){
            cost.val(parseFloat(0).toFixed(2));
        }
        SetSellPrice();
    });//ENDS COST FIELD CHANGES

    utility.change(function(){//UTILITY FIELD CHANGES
        if (utility.val()==""){
            utility.val(parseFloat(0).toFixed(2));
        }
        SetSellPrice();
    });//ENDS UTILITY FIELD CHANGES

   price.change(function(){//PRICE FIELD CHANGES
        if (price.val()==""){
            price.val(parseFloat(0).toFixed(2));
        }
        SetSellPrice();
    });//ENDS PRICE FIELD CHANGES

    });//document ready closes

    function SetSellPrice (){

        console.log("called");

        var sell_price = $('#id_product_sellprice');
        var cost = $('#id_product_cost');
        var autoprice = $('#id_product_autoprice');
        var utility = $('#id_product_utility');
        var price = $('#id_product_price');
        var use_taxes = $('#id_product_usetaxes');
        var taxes = $('#id_product_taxes');

        var price_to_set = 0;
        var tax=(taxes.val()/100)+1;
        if(autoprice.is(':checked')){
            if(use_taxes.is(':checked')){

                price_to_set = (cost.val()*(1+(utility.val()/100)))*tax;
            }
            else{
                price_to_set = cost.val()*(1+(utility.val()/100));
            }
        }
        else{
            if(use_taxes.is(':checked')){
                price_to_set = price.val()*tax;
            }
            else{
                price_to_set = price.val();
            }
        }

        sell_price.val(parseFloat(price_to_set).toFixed(2));
    }

})(django.jQuery);