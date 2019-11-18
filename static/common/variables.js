let data = {}

function updateData(payload) {
    data = payload
}


// Load pages
let Cameras = load('static/modules/pages/cameras/cameras.js');
let Dashboard = load("static/modules/pages/dashboard/dashboard.html")
let Arm = load("static/modules/pages/arm/arm.html")
let Map = load("static/modules/pages/map/map.html")

let pages = {
    "Dashboard": Dashboard,
    "Cameras": Cameras,
    "Arm": Arm,
    "Map": Map
}

let activePage = 'Dashboard'
function changeActivePage(page) {
    activePage = page
}

function load(url)
{
    let req = new XMLHttpRequest();
    req.open("GET", url, false);
    req.send(null);

    return(req.responseText); 
}

export {
    data,
    updateData,
    activePage,
    changeActivePage,
    load,
    pages
}
