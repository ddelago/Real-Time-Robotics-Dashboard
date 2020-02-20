import { activePage, changeActivePage, pages, socket } from '../../common/variables.mjs';
import {home, map, camera, arm} from '../../assets/icons.mjs';

$(".home").html(home);
$(".camera").html(camera);
$(".arm").html(arm);
$(".map").html(map);

// For each nav-link element, add an onClick function to change active state
document.querySelectorAll(".nav-link").forEach(function(navLink) {
    // Initialize to Dashboard
    $('#mainContent').html(pages[activePage]);

    // Change page on sidebar click
    navLink.addEventListener("click", function(e){
        // Remove old active
        document.querySelector('a.active').classList.remove('active');

        // Set new active
        navLink.classList.add('active');
        
        // Change active page 
        let newPage = e.target.id;
        document.querySelector(".active-page-header").innerHTML = `${newPage}`; 
        if (newPage != activePage) {
            $('#mainContent').html(pages[newPage]);
        }
        changeActivePage(newPage);
        socket.emit('page_change', {page: newPage});
    });
});