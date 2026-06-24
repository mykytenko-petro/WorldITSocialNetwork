import { renderHTML } from "/static/js/utils/renderHTML.js"

export const chatNotificationCount = (mode, element) => {
    const wrapper = document.createElement("div")
    wrapper.className = "chat-notification-wrapper"

    wrapper.appendChild(renderHTML(/* html */ `
        <p class="notification-count" data-role="${mode}"></p>
    `))

    element.replaceWith(wrapper)

    wrapper.appendChild(element)
}

