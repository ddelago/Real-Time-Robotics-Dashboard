let data = {}

function updateData(payload) {
    data = payload
}

let activePage = 'Dashboard'
function changeActivePage(page) {
    activePage = page
}

export {
    data,
    updateData,
    activePage,
    changeActivePage
}
