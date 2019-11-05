import { activePage, changeActivePage } from '../../common/variables.js';

// For each nav-link element, add an onClick function to change active state
document.querySelectorAll(".nav-link").forEach(function(navLink) {
    navLink.addEventListener("click", function(e){
        // Remove old active
        document.querySelector('a.active').classList.remove('active');
        // Set new active
        navLink.classList.add('active');

        // Change active page variable
        changeActivePage(e.target.innerHTML);
        document.querySelector(".active-page-header").innerHTML = `${activePage}`;
    });
});