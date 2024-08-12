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

    // Tooltip initalisation
    var tooltipped = document.querySelectorAll('.tooltipped');
    M.Tooltip.init(tooltipped);

    // Apply saved nav alert changes
    applySavedNavAlert();
  });


  function updateNavAlert(navText, navColor) {
    let navAlert = document.getElementById("nav-alert");
    navAlert.className = "";
    navAlert.innerText = navText;
    navAlert.classList.add(navColor, "center-align");
    
    // Save the nav alert text and color to localStorage
    localStorage.setItem('navText', navText);
    localStorage.setItem('navColor', navColor);
    
    // Ensure the nav alert is visible when updated
    localStorage.setItem('navAlertVisible', 'true');
    navAlert.classList.remove('hide');
}

function applySavedNavAlert() {
    let navText = localStorage.getItem('navText');
    let navColor = localStorage.getItem('navColor');
    let navAlertVisible = localStorage.getItem('navAlertVisible');

    if (navText && navColor) {
        let navAlert = document.getElementById("nav-alert");

        // Clear all existing classes
        navAlert.className = "";

        // Apply the saved text and classes
        navAlert.innerText = navText;
        navAlert.classList.add(navColor, "center-align");

        // Apply visibility based on saved state
        if (navAlertVisible === 'false') {
            navAlert.classList.add('hide');
        } else {
            navAlert.classList.remove('hide');
        }
    }
}

function hideNavAlert() {
    let navAlert = document.getElementById("nav-alert");
    navAlert.classList.add("hide");

    // Update localStorage to remember that the nav alert is hidden
    localStorage.setItem('navAlertVisible', 'false');
}