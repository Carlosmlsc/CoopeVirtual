
$(document).on('ready', mainListProducts );


//MAIN
//------------------------------------------------------------------------------------------
function mainListProducts() {

    //EVENTS

    loadObjects('products');

    browserObjectEvents();



}//MAIN FUNCTION

function browserObjectEvents(){



}

function loadObjects(model) {

    $.get(`/api/${model}/`, function (data) {

        fillTable(data)

    });


}

function fillTable(data) {

    $.each(data, function(i) {

        var newRow=`<tr class="${data[i].code}">
                        <td>${data[i].code}</td>
                        <td>${data[i].barcode}</td>
                        <td>${data[i].description} </td>
                        <td>${data[i].barcode} </td>
                        <td>${data[i].barcode} </td>
                        <td>${data[i].barcode} </td>
                        <td>${data[i].barcode} </td>
                        <td>${data[i].barcode} </td>
                    </tr>`;

        $('.list-table-body').append(newRow);


    });

    $('.list-table').dynatable();



}

