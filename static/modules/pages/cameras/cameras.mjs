import { html } from '/static/modules/pages/cameras/html.mjs';


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
