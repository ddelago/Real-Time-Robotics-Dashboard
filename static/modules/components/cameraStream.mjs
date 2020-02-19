export { newCameraStream };

function newCameraStream(name, source) {
  return {
    // stream parameters
    source: source,
    name: name,

    // A string of styles. 
    styles: `
      <style>
        .camera-stream {
          width: 550;
          height: auto;
        }

        .full-width {
          width: 80vw;
        }
      </style>
    `,

    // Returns a string of html to be rendered
    // Stream comes wrapped in a 'col' so they'll stack nicely with bootstrap
    html: function() {
      // Div wrapper
      let div = document.createElement('div');
      div.classList.add("col");

      // Video element
      let video = document.createElement('video');
      video.classList.add("camera-stream");
      video.autoplay = true;
      video.muted = true;

      // Video source
      let source = document.createElement('source');
      source.src = this.source;
      source.type = 'video/mp4';

      let title = document.createElement('h4');
      title.innerText = this.name;

      video.innerHTML = source.outerHTML;
      div.innerHTML = this.styles + title.outerHTML + video.outerHTML;


      return div.outerHTML;
    }
  }
}
