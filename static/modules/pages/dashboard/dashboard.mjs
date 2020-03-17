import { socket, serverConnected, setServerConnected } from '/static/common/variables.mjs';

// Controller buttons
$("#connect-controller").click(function(){
    socket.emit('connect_controller');
})

$("#submit-button").click(function() {
    if(serverConnected == false) {
        var ip = $("#rover_address").val();
        var port = $("#rover_port").val();
        socket.emit('connect_to_rover', {ip: ip, port: port});
        $("#submit-button").html("Disconnect");
        $("#submit-button").removeClass("btn-primary");
        $("#submit-button").addClass("btn-danger");
        setServerConnected(true);
    }
    else {
        socket.emit('disconnect_from_rover');
        $("#submit-button").html("Connect");
        $("#submit-button").removeClass("btn-danger");
        $("#submit-button").addClass("btn-primary");
    }
})

$("#activate-led").click(function() {
    // red, green, blue
    var colorList = [0,1,2]
    var color = colorList[Math.floor(Math.random()*colorList.length)];
    socket.emit('send_command', {command: 'led', data: [color]});
})