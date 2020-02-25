
$(".video-container .card").click(function() {
    $(".full-screen-modal").html($(this).clone());
    $(".full-screen-modal").removeClass("hidden");
})

$(".full-screen-modal").click(function() {
    $(this).html("");
    $(this).addClass("hidden");
})