import { activePage, changeActivePage, pages } from '../../common/variables.js';

// For each nav-link element, add an onClick function to change active state
document.querySelectorAll(".nav-link").forEach(function(navLink) {
    // Initialize to Dashboard
    $('#mainContent').html(pages[activePage]);

    // Change page on sidebar click
    navLink.addEventListener("click", function(e){
        // Remove old active
        document.querySelector('a.active').classList.remove('active');

        // Set new active
        navLink.classList.add('active');
        
        // Change active page 
        let newPage = e.target.innerHTML;
        document.querySelector(".active-page-header").innerHTML = `${newPage}`; 
        if (newPage != activePage) {
            $('#mainContent').html(pages[newPage]);
        }
        changeActivePage(newPage);
    });
});