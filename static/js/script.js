 $(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('select').formSelect();
    $('.datepicker').datepicker({
        format: "dd mmm yyyy",
        yearRange: 0,
        showClearBtn: true,
        i18n:{
            done: "Select"
        }
    });
    $('.modal').modal();
  });