import { Header } from './modules/header/header.js';
import { Sidebar } from './modules/sidebar/sidebar.js';
import { PageContainer } from './modules/pages/pageContainer.js';

let app = document.getElementById("app");

app.innerHTML = 
`
${Header()}
<div class="container-fluid">
    <div class="row">
    </div>
</div>
`;

let appRow = app.querySelector(".row");

appRow.innerHTML = Sidebar() + PageContainer();
