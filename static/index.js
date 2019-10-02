import { Header } from './modules/header/header.js';
import { Sidebar, SidebarEvents } from './modules/sidebar/sidebar.js';
import { PageContainer } from './modules/pages/pageContainer.js';
import { data, activePage } from './common/variables.js';
import { initSocket } from './common/socket.js';

// Pages
import { Dashboard } from './modules/pages/dashboard/dashboard.js';
import { Cameras } from './modules/pages/cameras/cameras.js';
import { Arm } from './modules/pages/arm/arm.js';
import { Map } from './modules/pages/map/map.js';

// Pass this to pages that need to update and override socket methods
let socket = initSocket();

let app = document.getElementById("app");

app.innerHTML =
`
${Header()}
<div class="container-fluid">
    <div class="row">
    </div>
</div>
`;

let dashboard = app.querySelector(".row");

// Add HTML
dashboard.innerHTML += Sidebar()
dashboard.innerHTML += PageContainer();

// Add Events
SidebarEvents(dashboard);

// Key is the name of the page
// Value is the function that returns the html of that page
let pages = {
    "Dashboard": Dashboard,
    "Cameras": Cameras,
    "Arm": Arm,
    "Map": Map,
}

// TODO: Need replace dashboard below and have way to reload DOM whenever the page is changed
// Refresh active page content data
let refreshPage = setInterval(function() {
    dashboard.querySelector(".active-page-content").innerHTML = `Incoming Message: ${data.data}`;

    // Updates page content based on activePage
    dashboard.querySelector('#mainContent').innerHTML = pages[activePage]();

    // if( activePage != 'dashboard') {
    //     console.log('stopped')
    //     clearInterval(refreshPage);
    // }
}, 100);
