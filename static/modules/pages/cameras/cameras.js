
let cameras = [
  [1, 'Camera 1', '/static/assets/test_video.mp4'],
  [2, 'Camera 2', '/static/assets/test_video.mp4'],
  [3, 'Camera 3', '/static/assets/test_video.mp4'],
  [4, 'Camera 4', '/static/assets/test_video.mp4'],
  [5, 'Camera 5', '/static/assets/test_video.mp4'],
  [6, 'Camera 6', '/static/assets/test_video.mp4'],
]

let i = 0;
$('document').ready(() => {
  cameras.forEach(camera => {
    let id = camera[0];
    let name = camera[1];
    let source = camera[2];

    if (i % 2 == 0) {
      $('#camerasContainer').append('<div class="row"></div>');
    }

    let el = $(`
      <div id="cameraContainer">
        <h1>
          ${name}
          <img class="fullscreen-button" id="fullscreen-${id}" src="https://icon-library.net/images/fullscreen-icon-vector/fullscreen-icon-vector-21.jpg" width="25px"></img>
        </h1>
        <video autoplay muted controls>
          <source src="${source}" type='video/mp4;codecs="avc1.42E01E, mp4a.40.2"'></source>
        </video>
      </div>
    `);

    $('#camerasContainer').children('.row').last().append(el)

    $(`#fullscreen-${id}`).click(function() {
      // Start the popout
    })

    i++;
  });

})

