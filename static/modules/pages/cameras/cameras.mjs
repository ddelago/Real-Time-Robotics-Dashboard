import { newCameraStream } from '/static/modules/components/cameraStream.mjs';

let stream_one = newCameraStream('ZED', 'static/assets/test_video.mp4');
$("#cam-one").html(stream_one.html());
$("#cam-one video").attr('width',"100%");

let stream_two = newCameraStream('Arm Cam', 'static/assets/test_video.mp4');
$("#cam-two").html(stream_two.html());
$("#cam-two video").attr('width',"100%");

$(".video-container .card").click(function() {
    $(".full-screen-modal").html($(this).clone());
    $(".full-screen-modal").removeClass("hidden");
})

$(".full-screen-modal").click(function() {
    $(this).html("");
    $(this).addClass("hidden");
})