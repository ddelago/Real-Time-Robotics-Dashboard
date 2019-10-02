export { newCameraStream };

// Example
// let stream = newCameraStream("/some/video/source.mp4", "Camera 5");
// // Render this
// body.innerHTML += stream.html();

function newCameraStream(source, name) {
  return {
    // stream parameters
    source: source,
    name: name,

    // A string of styles. This could be included in the html method,
    // but i like to keep it separate
    styles: `
      <style>
        .camera-stream {
          width: 550;
          height: auto;
        }

        .camera-stream:focus {
          width: 80vw;
          height: auto;
        }
      </style>
    `,

    // Returns a string of html to be rendered
    // Stream comes wrapped in a 'col' so they'll stack nicely with bootstrap
    html: function() {
      let div = document.createElement('div');
      div.classList.add("col");

      div.innerHTML = `
        ${this.styles}
        <h3>${this.name}</h3>
        <video class="camera-stream" autoplay muted>
          <source src="${this.source}" type="video/mp4">
          Your browser doesn't support videos
        </video>
      `

      return div.outerHTML;
    }
  }
}
