
let cameras = [
  ['Camera 1', '/static/assets/test_video.mp4'],
  ['Camera 2', '/static/assets/test_video.mp4'],
  ['Camera 3', '/static/assets/test_video.mp4'],
  ['Camera 4', '/static/assets/test_video.mp4'],
  ['Camera 5', '/static/assets/test_video.mp4'],
  ['Camera 6', '/static/assets/test_video.mp4'],
]

let i = 0;
$('document').ready(() => {
  cameras.forEach(camera => {
    let name = camera[0];
    let source = camera[1];

    if (i % 2 == 0) {
      $('#camerasContainer').append('<div class="row"></div>');
    }

    let el = $(`
      <div id="cameraContainer">
        <h1>
          ${name}

        </h1>
        <video autoplay muted controls>
          <source src="${source}" type='video/mp4;codecs="avc1.42E01E, mp4a.40.2"'></source>
        </video>
      </div>
    `);

    $('#camerasContainer').children('.row').last().append(el)

    i++;
  });

})

