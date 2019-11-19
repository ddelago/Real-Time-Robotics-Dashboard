let data = {}

function updateData(payload) {
    data = payload
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

function loadPage(page)
{
    var page_html = {
        "Dashboard": "static/modules/pages/dashboard/dashboard.html",
        "Cameras": "static/modules/pages/cameras/cameras.js",
        "Arm": "static/modules/pages/arm/arm.html",
        "Map": "static/modules/pages/map/map.html"
    }
    
    var page_script = {
        "Dashboard": "static/modules/pages/dashboard/dashboard.js",
        "Cameras": "static/modules/pages/cameras/cameras.js",
        "Arm": "static/modules/pages/arm/arm.js",
        "Map": "static/modules/pages/map/map.js"
    }

    let html = load(page_html[page]);
    let script = load(page_script[page]);

    return(`${html}<script type='module'>${script}</script>`); 
}

let pages = {
    "Dashboard": loadPage('Dashboard'),
    "Cameras": loadPage('Cameras'),
    "Arm": loadPage('Arm'),
    "Map": loadPage('Map')
}

export {
    data,
    updateData,
    activePage,
    changeActivePage,
    load,
    pages
}
