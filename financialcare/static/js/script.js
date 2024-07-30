document.addEventListener('DOMContentLoaded', function() {
    // Side Nav intialisation
    var sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // Modal Trigger
      var modaltrigger = document.querySelectorAll('.modal');
      M.Modal.init(modaltrigger);
  });