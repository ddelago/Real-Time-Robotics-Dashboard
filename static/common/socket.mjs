import { updateData } from './variables.mjs';
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

    return socket;
}