import { linkDiv, links } from "./createPostForm.js"
import { postLink, createPostLinkButton } from "./elements.js"

// links
function updateLinks() {
    for (let linkIndex = links.length; linkIndex > 0; linkIndex--) {
        links[linkIndex - 1].appendChild(createPostLinkButton())
    }
}

export function createPostLink() {
    linkDiv.appendChild(postLink())

    updateLinks()
}