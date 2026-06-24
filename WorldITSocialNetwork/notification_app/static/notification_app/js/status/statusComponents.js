import { renderHTML } from "/static/js/utils/renderHTML.js"

export const statusBubble = (element, userId) => {
    const wrapper = document.createElement("div")

    wrapper.appendChild(renderHTML(/* html */`
        <div class="status-bubble" data-user-id="${userId}"></div>
    `))

    element.replaceWith(wrapper)

    wrapper.appendChild(element)
}