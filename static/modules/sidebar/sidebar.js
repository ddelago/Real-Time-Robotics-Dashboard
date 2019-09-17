import { sidebarContainer, sidebarItem } from './html.js';
import { activePage, changeActivePage } from '../../common/variables.js';
export { Sidebar, SidebarEvents };

function Sidebar() {
    const sidebar = new DOMParser().parseFromString(sidebarContainer, "text/html");
    sidebar.querySelector(".nav").innerHTML = sidebarItem

    return sidebar.body.innerHTML;
}

function SidebarEvents(element){
    // For each nav-link element, add an onClick function to change active state
    element.querySelectorAll(".nav-link").forEach(function(navLink) {
        navLink.addEventListener("click", function(e){
            // Remove old active
            element.querySelector('a.active').classList.remove('active');
            // Set new active
            navLink.classList.add('active');

            // Change active page variable
            changeActivePage(e.target.innerHTML);
            element.querySelector(".active-page-header").innerHTML = `${activePage}`;
        });
    });
}