import { data, load, socket } from './common/variables.mjs';

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

// Refresh active page content data
// let dashboard = app.querySelector("#app .row");
let refreshPage = setInterval(function() {
    $(".active-page-content").html(`Incoming Message: ${data.data}`)
    // dashboard.querySelector(".active-page-content").innerHTML = `Incoming Message: ${data.data}`;
}, 100);
