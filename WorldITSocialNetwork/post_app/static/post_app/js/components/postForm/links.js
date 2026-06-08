import { postForm } from "./form.js"

// dom
const linkDiv = postForm.querySelector(".links > div")
const links = postForm.querySelectorAll(".links > div")

// components
const postLink = (isPrimary) => {
    const div = document.createElement("div")
    const input = document.createElement("input")

    div.className = "link-row"

    input.type = "url"
    input.name = "links"

    div.appendChild(input)
    if (isPrimary) div.toggleAttribute('primal')

    input.addEventListener('focus', (event) => {
        div.appendChild(createPostLinkButton())
        if (!isPrimary) div.appendChild(removePostLinkButton())
    })

    input.addEventListener("blur", () => {
        setTimeout(() => {
            div.removeChild(div.lastChild)
            if (!isPrimary) div.removeChild(div.lastChild)
        }, 80)
    })

    return div
}

const createPostLinkButton = () => {
    const button = document.createElement("button")
    const img = document.createElement("img")

    button.className = "post-button"
    button.type = "button"

    img.src = "/static/icon/add-post-link.svg"

    button.appendChild(img)
    button.addEventListener("click", () => {
        linkDiv.appendChild(postLink())
    })

    return button
}

const removePostLinkButton = () => {
    const button = document.createElement("button")
    const img = document.createElement("img")

    button.className = "post-button"

    img.src = "/static/icon/remove-post-link.svg"

    button.appendChild(img)
    button.addEventListener("click", () => {
        button.closest("div").remove()
    })

    return button
}

// logic
linkDiv.appendChild(postLink(true))
