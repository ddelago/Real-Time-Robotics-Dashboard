export { html };

import { newCameraStream } from '../../components/cameraStream.js';


// Test data, this will be from the rover eventually i guess
let cameras = [
  (1, 'test camera 1'),
  (2, 'test camera 2'),
  (3, 'test camera 3'),
  (4, 'test camera 4'),
  (5, 'test camera 5'),
  (6, 'test camera 6'),
];

// Returns a new div with the 'row' bootstrap class
function newRow() {
  let row = document.createElement('div');
  row.classList.add("row");
  return row;
}

// Parent element
let html = document.createElement('div');


// Set up the camera streams
let count = 0;
let stream = {};

// Containing element
let camerasContainer = document.createElement('div');

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

html.innerHTML += camerasContainer.outerHTML;
