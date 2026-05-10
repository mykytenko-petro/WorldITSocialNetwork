import { createPostLink } from "./links.js"

export const postLink = () => {
    const div = document.createElement("div")
    const input = document.createElement("input")

    div.appendChild(input)

    return div
}

export const createPostLinkButton = () => {
    const button = document.createElement("button")
    const img = document.createElement("img")

    button.className = "post-button"
    button.type = "button"
    button.onclick = createPostLink

    img.src = "/static/icon/add-post-link.svg"

    button.appendChild(img)

    return button
}

export const removePostLinkButton = () => {
    const button = document.createElement("button")
    const img = document.createElement("img")

    button.className = "post-button"

    img.src = "/static/icon/remove-post-link.svg"

    button.appendChild(img)

    return button
}