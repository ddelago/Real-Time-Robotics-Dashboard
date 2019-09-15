let data = {}

function updateData(payload) {
    data = payload
}

function stopContentUpdate(intervalId){
    clearInterval(intervalId);
}

export {
    data,
    updateData,
    stopContentUpdate
}