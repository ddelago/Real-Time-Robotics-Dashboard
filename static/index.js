import { Header } from './modules/header/header.js';
import { Sidebar } from './modules/sidebar/sidebar.js';
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
dashboard.innerHTML = Sidebar() + PageContainer();

// TODO: Need replace dashboard below and have way to reload DOM whenever the page is changed
// Refresh active page content
let refreshPage = setInterval(function() {
    dashboard.querySelector(".active-page-content").innerHTML = data.data;

    if( activePage != 'dashboard') {
        console.log('stopped')
        clearInterval(refreshPage);
    } 
}, 250);