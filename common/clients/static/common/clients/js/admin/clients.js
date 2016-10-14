/**
 * Created by emanuelziga on 17/6/16.
 */
(function($) {
    $(document).ready(function($) {

    var id = $('#id_client_id');
    var idt = $('#id_client_id_type');
    var prev_id_val = id.val();

    if(id.val()==''){
      id.val('-');
    }


    idt.change(function() {

        if(idt.val()=='noid'){

            id.val('-');
        }
        else{
            if(prev_id_val==''){
              id.val('');
            }
            else{
               id.val(prev_id_val);
            }
        }

    });

    });
})(django.jQuery);