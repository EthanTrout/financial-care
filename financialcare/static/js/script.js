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
  });