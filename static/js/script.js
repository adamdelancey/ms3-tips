  $(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
    $('.datepicker').datepicker({
        format: "dd mmm yyyy",
        yearRange: 0,
        showClearBtn: true,
        i18n:{
            done: "Select"
        }
    });
  });
        