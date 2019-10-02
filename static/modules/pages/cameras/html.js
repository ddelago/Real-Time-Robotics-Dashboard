export { html };

import { newCameraStream } from '../../components/cameraStream.js';


// Test data, this will be from the rover eventually i guess
let cameras = [1, 2, 3, 4, 5];

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

cameras.forEach(cam => {
  // add a new row every two streams so they'll stack well
  if (count % 2 == 0) {
    camerasContainer.innerHTML += newRow().outerHTML;
    if (count == 2) { count = 0 };
  }
  count++;

  // Create a new stream
  // You'll get the source from the rover i'm assuming
  // Here's i'm just using a stupid test video
  stream = newCameraStream("/static/assets/test_video.mp4", "camera " + cam);

  // Add the camera stream to the latest row
  camerasContainer.lastChild.innerHTML += stream.html();
});

html.innerHTML += camerasContainer.outerHTML;
