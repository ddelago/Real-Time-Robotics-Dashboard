import { newCameraStream } from '/static/modules/components/cameraStream.mjs';
import { socket, getControllerState } from '/static/common/variables.mjs';

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
    socket.emit('connect_controller');
})

$("#get-controller").click(function(){
    getControllerState();
}) 

$("#submit-button").click(function() {
    var ip = $("#rover_address").val();
    var port = $("#rover_port").val();
    socket.emit('connect_to_rover', {ip: ip, port: port});
})