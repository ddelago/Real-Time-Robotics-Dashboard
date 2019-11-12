import { data, activePage, load } from './common/variables.js';
import { initSocket } from './common/socket.js';

// Initialize connection
let socket = initSocket();

// Load pages
let Sidebar = load("static/modules/sidebar/sidebar.html");
let Header = load("static/modules/header/header.html")
let Cameras = load("static/modules/pages/cameras/cameras.html");
let pageContainer = load("static/modules/pages/pageContainer/pageContainer.html");
let Dashboard = load("static/modules/pages/dashboard/dashboard.html")
let Arm = load("static/modules/pages/arm/arm.html")
let Map = load("static/modules/pages/map/map.html")

$("#app").html(
    `
    ${Header}
    <div class="container-fluid">
        <div class="row">
            ${Sidebar}
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
        $('#mainContent').html(pages[activePage]);
    }

    oldActivePage = activePage;
}, 100);
