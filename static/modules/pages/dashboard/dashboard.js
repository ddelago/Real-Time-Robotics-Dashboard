import { newCameraStream } from '../../components/cameraStream.js';

$(document).ready(function(){
    // Camera stream 1
    let stream_one = newCameraStream('Stream 1', 'static/assets/test_video.mp4');
    $("#cam-one").html(stream_one.html());
    $("#cam-one video").attr('width',"100%");

    // Camera stream 2
    let stream_two = newCameraStream('Stream 2', 'static/assets/test_video.mp4');
    $("#cam-two").html(stream_two.html());
    $("#cam-two video").attr('width',"100%");

    // Camera stream 3
    let stream_three = newCameraStream('Stream 3', 'static/assets/test_video.mp4');
    $("#cam-three").html(stream_three.html());
    $("#cam-three video").attr('width',"100%");
});