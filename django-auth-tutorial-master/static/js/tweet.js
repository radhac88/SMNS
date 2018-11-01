/*$("i").click(function () {
  $("input[type='file']").trigger('click');
});

$('input[type="file"]').on('change', function() {
  var val = $(this).val();
  $(this).siblings('span').text(val);
})*/

$(document).ready(function(){
    $("p").click(function(){
        $(this).hide();
    });
});
