import { newCameraStream } from '../../components/cameraStream.js';

$(document).ready(function(){
    // Camera stream 1
    let stream_one = newCameraStream('Stream 1', 'static/assets/test_video.mp4');
    $("#cam-one").html(stream_one.html());

    // Camera stream 2
    let stream_two = newCameraStream('Stream 2', 'static/assets/test_video.mp4');
    $("#cam-two").html(stream_two.html());

    // Camera stream 3
    let stream_three = $('<img />', {
        src: 'static/assets/placeholder.jpg'
    });
    $("#cam-three").html(stream_three);
});