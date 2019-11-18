import { data, load } from './common/variables.js';
import { initSocket } from './common/socket.js';

// Initialize connection
let socket = initSocket();

// Load components
let Sidebar = load("static/modules/sidebar/sidebar.html");
let Header = load("static/modules/header/header.html")
let pageContainer = load("static/modules/pages/pageContainer/pageContainer.html");

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

// Need to figure out a way for scripts to re-evaluate after dynamic 
// insertion of html.

// Refresh active page content data
let dashboard = app.querySelector("#app .row");
let refreshPage = setInterval(function() {
    dashboard.querySelector(".active-page-content").innerHTML = `Incoming Message: ${data.data}`;
}, 100);
