import { initSocket } from './socket.mjs';

let socket = initSocket();

let data = {}
function updateData(payload) {
    data = payload
}

let activePage = 'Dashboard'
function changeActivePage(page) {
    activePage = page
    if(page != 'Dashboard'){
        stopControllerLoop();
    
}

function load(url)
{
    let req = new XMLHttpRequest();
    req.open("GET", url, false);
    req.send(null);

    return(req.responseText); 
}

// To avoid injected scripts error, dynamic pages have to be loaded with their hmtl and script seperate
function loadPage(page)
{
    var page_html = {
        "Dashboard": "static/modules/pages/dashboard/dashboard.html",
        "Cameras": "static/modules/pages/cameras/cameras.mjs",
        "Arm": "static/modules/pages/arm/arm.html",
        "Map": "static/modules/pages/map/map.html"
    }
    
    var page_script = {
        "Dashboard": "static/modules/pages/dashboard/dashboard.mjs",
        "Cameras": "static/modules/pages/cameras/cameras.mjs",
        "Arm": "static/modules/pages/arm/arm.mjs",
        "Map": "static/modules/pages/map/map.mjs"
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

var controllerLoop;
function getControllerState(){
    // If loop already running, don't start another
    if(controllerLoop != null)
        return 
    controllerLoop = setInterval(function() { 
        socket.emit('get_controller_state');
        console.log('getting controller')
    }, 1000);
}

function stopControllerLoop(){
    clearTimeout(controllerLoop);
}

export {
    data,
    updateData,
    activePage,
    changeActivePage,
    load,
    pages,
    socket,
    getControllerState
}
