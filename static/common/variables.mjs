import { initSocket } from './socket.mjs';
let socket = initSocket();

let data = {}
function updateData(payload) {
    data = payload
}

var serverConnected = false;
function setServerConnected(val) {
    serverConnected = val;
}

let activePage = 'Dashboard';
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

// To avoid injected scripts error, dynamic pages have to be loaded with their hmtl and script seperate
function loadPage(page)
{
    var page_html = {
        "Dashboard": "static/modules/pages/dashboard/dashboard.html",
        "Cameras": "static/modules/pages/cameras/cameras.html",
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


var controllerConnected = false;
function setControllerStatus(val) {
    controllerConnected = val
}

function getControllerState(){
    socket.emit('send_controller_state');
}

function stopControllerState(){
    socket.emit('pause_controller_state');
}

function updateControllerData(payload){
    var drive = payload.drive > 124 && payload.drive < 130? 127 : payload.drive;
    var steer = payload.steer > 110 && payload.steer < 150? 127 : payload.steer;
    $("#drive-value").html(drive)
    $("#steer-value").html(steer)

    if(drive >= 127){
        $("#drive-status").html("Forward");
        $("#drive-status").removeClass('text-danger');
        $("#drive-status").addClass('text-success');
    }

    if(drive < 127){
        $("#drive-status").html("Reverse");
        $("#drive-status").addClass('text-danger');
        $("#drive-status").removeClass('text-success');
    }

    if(steer >= 127){
        $("#steer-status").html("Right");
    }

    if(steer < 127){
        $("#steer-status").html("Left");
    }
}

export {
    data,
    updateData,
    activePage,
    changeActivePage,
    load,
    pages,
    socket,
    getControllerState,
    stopControllerState,
    controllerConnected,
    setControllerStatus,
    updateControllerData,
    serverConnected,
    setServerConnected
}
