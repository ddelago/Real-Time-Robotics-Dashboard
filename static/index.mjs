import { load, pages } from './common/variables.mjs';

// Load components
let Sidebar = load("static/modules/sidebar/sidebar.html");
let Header = load("static/modules/header/header.html")

// Page container is just a wrapper for the actual page content.
let pageContainer = load("static/modules/pages/pageContainer/pageContainer.html");

// Insert them into the dashboard
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

// Show the main dashboard tab
$('#mainContent').html(pages['Dashboard']);