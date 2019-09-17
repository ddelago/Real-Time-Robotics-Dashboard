import { pageContainer } from './html.js';
import { data } from '../../../common/variables.js';
export { Dashboard };

function Dashboard() {
    const pageContainerDom = new DOMParser().parseFromString(pageContainer, "text/html");
    pageContainerDom.querySelector(".active-page-content").innerHTML = data;

    return pageContainerDom.body.innerHTML;
}