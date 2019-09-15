let data = {}

function updateData(payload) {
    data = payload
}

let activePage = ''
function changeActivePage(page) {
    activePage = page
}

export {
    data,
    updateData,
    activePage,
    changeActivePage
}