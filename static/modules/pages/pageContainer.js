import { pageContainer } from './html.js';
import { data, activePage } from '../../common/variables.js';
import { Dashboard } from './dashboard/dashboard.js';
import { Cameras } from './cameras/cameras.js';
import { Arm } from './arm/arm.js';
import { Map } from './map/map.js';
export { PageContainer };

function PageContainer() {
    const pageContainerDom = new DOMParser().parseFromString(pageContainer, "text/html");
    pageContainerDom.querySelector(".active-page-content").innerHTML = `Incoming Message: ${data.data}`;

    pageContainerDom.querySelector(".active-page-header").innerHTML = `${activePage}`;

    return pageContainerDom.body.innerHTML;
}

function SidebarEvents(element){
    // For each nav-link element, add an onClick function to change active state
    element.querySelectorAll(".nav-link").forEach(function(navLink) {
        navLink.addEventListener("click", function(e){
            // Change active page variable
            changeActivePage(e.target.innerHTML);
            // Remove old active
            element.querySelector('a.active').classList.remove('active');
            // Set new active
            navLink.classList.add('active');
        });
    });
}