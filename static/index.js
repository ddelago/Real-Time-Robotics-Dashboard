import { Header } from './modules/header/header.js';
import { Sidebar } from './modules/sidebar/sidebar.js';
import { PageContainer, updatePageContent } from './modules/pages/pageContainer.js';
import { initSocket } from './common/socket.js';
import { stopContentUpdate } from './common/variables.js'

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

// var refresh = setInterval(updatePageContent(dashboard), 1000);
setInterval(updatePageContent(dashboard), 1000);