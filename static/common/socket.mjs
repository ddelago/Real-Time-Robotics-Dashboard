import { updateData } from './variables.mjs';
export { initSocket };

function initSocket() {
    let socket = io();

    socket.on('connect', function() {
        socket.emit('message', {data: 'I\'m connected!'});
        console.log("Connected to server")
    });

    socket.on('data', function(payload) {
        updateData(payload);
    })

    return socket;
}