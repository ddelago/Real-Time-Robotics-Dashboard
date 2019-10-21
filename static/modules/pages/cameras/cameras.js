import { html } from './html.js';

export { Cameras };

function Cameras() {
    // This is really bad and i don't like this
    // Adds click listeners to the videos
    setTimeout(() => {
        let videos = document.querySelectorAll('video');
        videos.forEach(video => {
            video.addEventListener('click', vid => {
                let cl = vid.srcElement.classList;
                // .full-width just makes the width 80vw
                if (!cl.contains('full-width')) {
                    cl.add('full-width');
                } else {
                    cl.remove('full-width');
                }
            })
        });
    }, 100);

    return html.innerHTML;
}
