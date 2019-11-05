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

export {
    data,
    updateData,
    activePage,
    changeActivePage,
    load
}
