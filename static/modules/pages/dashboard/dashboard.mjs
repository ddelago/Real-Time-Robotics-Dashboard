import { newCameraStream } from '/static/modules/components/cameraStream.mjs';
import { socket } from '/static/common/variables.mjs';

// Camera stream 1
let stream_one = newCameraStream('ZED', 'static/assets/test_video.mp4');
$("#cam-one").html(stream_one.html());
$("#cam-one video").attr('width',"100%");

// Camera stream 2
let stream_two = newCameraStream('Sample Return', 'static/assets/test_video.mp4');
$("#cam-two").html(stream_two.html());
$("#cam-two video").attr('width',"100%");

// Camera stream 3
let stream_three = newCameraStream('Mast', 'static/assets/test_video.mp4');
$("#cam-three").html(stream_three.html());
$("#cam-three video").attr('width',"100%");

// Controller buttons
$("#connect-controller").click(function(){
    socket.emit('connect_controller')
})

$("#get-controller").click(function(){
    socket.emit('get_controller_state');
}) 