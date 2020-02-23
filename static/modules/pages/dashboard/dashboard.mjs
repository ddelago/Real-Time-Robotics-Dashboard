import { newCameraStream } from '/static/modules/components/cameraStream.mjs';
import { socket, getControllerState, controllerConnected, setControllerStatus, serverConnected, setServerConnected } from '/static/common/variables.mjs';

// Camera stream 1
let stream_one = newCameraStream('ZED', 'static/assets/test_video.mp4');
$("#cam-one").html(stream_one.html());
$("#cam-one video").attr('width',"100%");

// Camera stream 2
let stream_two = newCameraStream('Arm Cam', 'static/assets/test_video.mp4');
$("#cam-two").html(stream_two.html());
$("#cam-two video").attr('width',"100%");

// Controller buttons
$("#connect-controller").click(function(){
    if(controllerConnected == false){
        socket.emit('connect_controller');
        $(this).html("Controller On");
        // $(this).prop('disabled', true);

        // Need to verify if the controller is actually connected
        setControllerStatus(true);
    }
})

$("#get-controller").click(function(){
    getControllerState();
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
    socket.emit('activate_led', {cmd: '0xCA', data: color});
})