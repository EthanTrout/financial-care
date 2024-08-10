document.addEventListener('DOMContentLoaded', function() {
    // Side Nav intialisation
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // Modal Trigger intialisation
    let modaltrigger = document.querySelectorAll('.modal');
    M.Modal.init(modaltrigger);

    // select intialisation
    let selects = document.querySelectorAll('select');
    M.FormSelect.init(selects);

    // Collapsible initalisation
    var collapsible = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsible);

    // Date picker Initalisation
    var datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker,{
      format:"yyyy,mm,dd",
      i18n:{done:"Select"}
    });

  });

  