import { pageContainer } from '../html.js/index.js';
import { data } from '../../common/variables.js';
export { PageContainer};

function PageContainer() {
    const pageContainerDom = new DOMParser().parseFromString(pageContainer, "text/html");
    pageContainerDom.querySelector(".active-page-content").innerHTML = data;

    return pageContainerDom.body.innerHTML;
}