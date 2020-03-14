jQuery(function ()
     {
       jQuery("#f_elem_city").autocomplete({
        source: function (request, response) {
         jQuery.getJSON(
          "https://secure.geobytes.com/AutoCompleteCity?key=7c756203dbb38590a66e01a5a3e1ad96&callback=?&q="+request.term,
          function (data) {
           response(data);
          }
         );
        },
        minLength: 3,
        select: function (event, ui) {
         var selectedObj = ui.item;
         jQuery("#f_elem_city").val(selectedObj.value);
        getcitydetails(selectedObj.value);
         return false;
        },
        open: function () {
         jQuery(this).removeClass("ui-corner-all").addClass("ui-corner-top");
        },
        close: function () {
         jQuery(this).removeClass("ui-corner-top").addClass("ui-corner-all");
        }
       });
       jQuery("#f_elem_city").autocomplete("option", "delay", 100);
      });
