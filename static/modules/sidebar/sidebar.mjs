import { activePage, changeActivePage, pages, socket } from '../../common/variables.mjs';
import {home, map, camera, arm} from '../../assets/icons.mjs';

// Add icons
$(".home").html(home);
$(".camera").html(camera);
$(".arm").html(arm);
$(".map").html(map);

var loadedPage = ''
// For each nav-link element (tab), add an onClick function to change active state
document.querySelectorAll(".nav-link").forEach(function(navLink) {
    // Load the new tab selected
    if(loadedPage != activePage) {
        $('#mainContent').html(pages[activePage]);
        loadedPage = activePage
    }

    // Change page on sidebar click
    navLink.addEventListener("click", function(e){
        // Remove old active tab
        document.querySelector('a.active').classList.remove('active');

        // Set new active tab
        navLink.classList.add('active');
        
        // Change active page 
        let newPage = e.target.id;

        // Change the title of the active dashboard page
        document.querySelector(".active-page-header").innerHTML = `${newPage}`; 

        // Update the content of the dashboard to the requested page
        if (newPage != activePage) {
            $('#mainContent').html(pages[newPage]);
        }
        changeActivePage(newPage);

        // This will let the server know what variables the user is looking at
        // Currently the server does nothing with this. Implementing this can 
        // lead to performance increases (loading a single page's data instead of all data)
        socket.emit('page_change', {page: newPage});
    });
});