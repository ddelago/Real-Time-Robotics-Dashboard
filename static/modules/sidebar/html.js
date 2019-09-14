export {sidebarContainer, sidebarItem}

const sidebarContainer = 
`
<nav class="col-md-2 d-none d-md-block bg-light sidebar">
    <div class="sidebar-sticky">
        <ul class="nav flex-column"></ul>
    </div>
</nav>
`
const sidebarItem = 
`
<li class="nav-item">
    <a class="nav-link active" href="#">
        <span data-feather="home"></span>
        Dashboard <span class="sr-only">(current)</span>
    </a>
</li>
<li class="nav-item">
    <a class="nav-link" href="#">
        <span data-feather="file"></span>
        Orders
    </a>
</li>
<li class="nav-item">
    <a class="nav-link" href="#">
        <span data-feather="shopping-cart"></span>
        Products
    </a>
</li>
<li class="nav-item">
    <a class="nav-link" href="#">
        <span data-feather="users"></span>
        Customers
    </a>
</li>
<li class="nav-item">
    <a class="nav-link" href="#">
        <span data-feather="bar-chart-2"></span>
        Reports
    </a>
</li>
<li class="nav-item">
    <a class="nav-link" href="#">
        <span data-feather="layers"></span>
        Integrations
    </a>
</li>
`