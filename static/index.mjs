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

// Initialize to Dashboard
$('#mainContent').html(pages['Dashboard']);