import { updateData, updateControllerData, updateControllerStatus, updateConnectionStatus, handleError} from './variables.mjs';
export { initSocket };

function initSocket() {
    let socket = io();

    // Listen for connection from server then reply
    socket.on('connect', function() {
        socket.emit('message', {data: 'I\'m connected!'});
        console.log("Connected to server")
    });

    // Listen for incoming data
    socket.on('data', function(payload) {
        updateData(payload);
        $(".active-page-content").html(`Incoming Message: ${payload.data}`)
    })

    socket.on('connection_status', function(payload) {
        updateConnectionStatus(payload);
    })

    socket.on('controller_status', function(payload) {
        updateControllerStatus(payload);
    })

    socket.on('controller_data', function(payload) {
        updateControllerData(payload);
    })

    socket.on('error', function(payload) {
        handleError(payload);
    })

    return socket;
}