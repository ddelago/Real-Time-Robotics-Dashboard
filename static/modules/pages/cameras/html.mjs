export { html };

import { newCameraStream } from '../../components/cameraStream.mjs';


// Test data, this will be from the rover eventually i guess
let cameras = [
  (1, 'test camera 1'),
  (2, 'test camera 2'),
  (3, 'test camera 3'),
];

// Returns a new div with the 'row' bootstrap class
function newRow() {
  let row = document.createElement('div');
  row.classList.add("row");
  return row;
}

// Set up the camera streams
let count = 0;
let stream = {};

cameras.forEach((id, name) => {
  // add a new row every two streams so they'll stack well
  if (count % 2 == 0) {
    camerasContainer.innerHTML += newRow().outerHTML;
    if (count == 2) { count = 0 };
  }
  count++;

  // Create a new stream
  // You'll get the source from the rover i'm assuming
  // Here i'm just using a stupid test video
  stream = newCameraStream(name, "/static/assets/test_video.mp4");

  // Add the camera stream to the latest row
  camerasContainer.lastChild.innerHTML += stream.html();
});

