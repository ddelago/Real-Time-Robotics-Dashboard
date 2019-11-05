import { Header } from './modules/header/header.js';
import { data, activePage, load } from './common/variables.js';
import { initSocket } from './common/socket.js';

// Pages
import { Dashboard } from './modules/pages/dashboard/dashboard.js';
import { Cameras } from './modules/pages/cameras/cameras.js';
import { Arm } from './modules/pages/arm/arm.js';
import { Map } from './modules/pages/map/map.js';

// Pass this to pages that need to update and override socket methods
let socket = initSocket();

// Load pages
let sidebar = load("static/modules/sidebar/sidebar.html");
let pageContainer = load("static/modules/pages/pageContainer/pageContainer.html");

$("#app").html(
    `
    ${Header()}
    <div class="container-fluid">
        <div class="row">
            ${sidebar}
            ${pageContainer}
        </div>
    </div>
    `
)

let app = document.getElementById("app");
let dashboard = app.querySelector(".row");

// Key is the name of the page
// Value is the function that returns the html of that page
let pages = {
    "Dashboard": Dashboard,
    "Cameras": Cameras,
    "Arm": Arm,
    "Map": Map,
}

let oldActivePage = '';

// Refresh active page content data
let refreshPage = setInterval(function() {
    dashboard.querySelector(".active-page-content").innerHTML = `Incoming Message: ${data.data}`;

    // Updates page content based on activePage
    // Only update if you change pages
    // This prevents 'changing' to the same page, updating every 100 ms
    if (activePage != oldActivePage) {
        dashboard.querySelector('#mainContent').innerHTML = pages[activePage]();
    }
    oldActivePage = activePage;
}, 100);
