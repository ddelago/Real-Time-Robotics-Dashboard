import { Header } from './modules/header/header.js';
import { Sidebar, SidebarEvents } from './modules/sidebar/sidebar.js';
import { PageContainer } from './modules/pages/pageContainer.js';
import { data, activePage } from './common/variables.js';
import { initSocket } from './common/socket.js';

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
dashboard.innerHTML += PageContainer() + Sidebar()

// Add Events
SidebarEvents(dashboard);

// TODO: Need replace dashboard below and have way to reload DOM whenever the page is changed
// Refresh active page content data
let refreshPage = setInterval(function() {
    dashboard.querySelector(".active-page-content").innerHTML = `Incoming Message: ${data.data}`;

    // if( activePage != 'dashboard') {
    //     console.log('stopped')
    //     clearInterval(refreshPage);
    // } 
}, 100);