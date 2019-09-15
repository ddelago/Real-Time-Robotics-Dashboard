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
        <span class="icon-here"></span>
        Dashboard
    </a>
</li>
<li class="nav-item">
    <a class="nav-link" href="#">
        Cameras
    </a>
</li>
<li class="nav-item">
    <a class="nav-link" href="#">
        Arm
    </a>
</li>
<li class="nav-item">
    <a class="nav-link" href="#">
        Map
    </a>
</li>
`