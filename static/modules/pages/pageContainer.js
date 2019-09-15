import { pageContainer } from './html.js';
import { data } from '../../common/variables.js';
export { PageContainer, updatePageContent };

function PageContainer(socket) {
    const pageContainerDom = new DOMParser().parseFromString(pageContainer, "text/html");
    pageContainerDom.querySelector(".active-page-content").innerHTML = data;

    return pageContainerDom.body.innerHTML;
} 

function updatePageContent(element) {
    element.querySelector(".active-page-content").innerHTML = data;
    console.log('page updated')
}