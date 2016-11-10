
$(document).on('ready', mainCreateProduct );

var department = $("#id_department");
const company = $("#id_company").val();

//MAIN
//------------------------------------------------------------------------------------------
function mainCreateProduct() {

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if(settings.type == "POST"){
                xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
            }
            if(settings.type == "PUT"){
                xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
            }
            if(settings.type == "PATCH"){
                xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
            }
        }
    });//ajax setup

    department.change(function() {

        $("#id_subdepartment option").hide();
        $(`#id_subdepartment option[familia=${$("#id_department").val()}]`).show();

        $('#id_subdepartment option').each(function () {
            if ($(this).css('display') != 'none') {
                $(this).prop("selected", true);
                return false;
            }
        });

    });

    $("#id_is_forsale").change(function() {

        if(this.checked) {
            enableDiv('.for-sale-div')
        }
        if(!this.checked) {
            disableDiv('.for-sale-div');
        }
        $("#id_is_forsale").attr("disabled", false);

    });

    $("#id_useinventory").change(function() {

        if(this.checked) {
            enableDiv('.inventory-div')
        }
        if(!this.checked) {
            disableDiv('.inventory-div');
        }
        $("#id_useinventory").attr("disabled", false);

    });

    initialDisables();

    $("#save_btn").on('click', function(ev) {
        ev.preventDefault();
        saveProduct();

    });

    $("#id_subdepartment").val( $("#id_sub_hidden").val());


}//MAIN FUNCTION


function initialDisables(){

    $('.inventory-div :input').attr("disabled", true);
    $('#id_useinventory').attr("disabled", false);
    $('.for-sale-div :input').attr("disabled", true);
    $('#id_is_forsale').attr("disabled", false);

    $("#id_department").trigger("change");

}

function disableDiv(selector){

    $(`${selector} :input`).attr("disabled", true);

};
function enableDiv(selector){

    $(`${selector} :input`).attr("disabled", false);

}

function saveProduct() {

    var isForSale = false;
    var useTaxes = false;
    var useInventory = false;


    if($('#id_is_forsale').prop("checked")) {
        isForSale=true;
    }
    if($('#id_usetaxes').prop("checked")) {
        useTaxes=true;
    }
    if($('#id_useinventory').prop("checked")) {
        useInventory=true;
    }

    $.ajax({
        method: "POST",
        url: "/products/add/",
        data:JSON.stringify({
            'company': company,
            'code': $("#id_code").val(),
            'unit': $("#id_unit").val(),
            'description': $("#id_description").val(),
            'department': $("#id_department").val(),
            'subdepartment': $("#id_subdepartment").val(),
            'cost': $("#id_cost").val(),
            'isForSale':isForSale,
            'barcode':$("#id_barcode").val(),
            'utility':$("#id_utility").val(),
            'price':$("#id_price").val(),
            'useTaxes':useTaxes,
            'taxes':$("#id_taxes").val(),
            'discount':$("#id_discount").val(),
            'sellprice':$("#id_sellprice").val(),
            'useInventory':useInventory,
            'inventory':$("#id_inventory").val(),
            'minimum':$("#id_minimum").val(),
        }),
        contentType:"application/json; charset=utf-8",
        dataType:"json"
    })
    .fail(function(data){
        console.log('fail');
        console.log(data)
    })
    .success(function(data){
        console.log('success');
        console.log(data)
    });//ajax

}