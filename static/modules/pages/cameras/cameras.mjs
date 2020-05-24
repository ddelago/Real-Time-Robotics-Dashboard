// If video stream clicked, add the stream to the full-screen modal
$(".video-container .card").click(function() {
    $(".full-screen-modal").html($(this).clone());
    $(".full-screen-modal").removeClass("hidden");
})

// If full-screen modal clicked, hide it.
$(".full-screen-modal").click(function() {
    $(this).html("");
    $(this).addClass("hidden");
})