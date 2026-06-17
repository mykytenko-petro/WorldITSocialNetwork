import { renderHTML } from "/static/js/utils/renderHTML.js"

document.addEventListener("dom:updateChatNotificationCount", (e) => {
    const notifications = document.querySelectorAll(".notification-count")

    notifications.forEach(element => {
        element.textContent = Cookies.get("chatNotificationCount") || 0
    })
})

const notificationCount = (count, element) => {
    if (Number(count) > 9) {
        count = "9+"
    }

    if (count == 0) {
        count = ''
    }

    const wrapper = document.createElement("div")
    // wrapper.className = "notification-wrapper"

    wrapper.appendChild(renderHTML(/* html */ `
        <p class="notification-count">${count}</p>
    `))

    element.replaceWith(wrapper)

    wrapper.appendChild(element)
}

export const chatNotificationCount = (element) => {
    notificationCount(
        Cookies.get("chatNotificationCount") || 2,
        element
    )
}

// assign notifications
const chatNotificationParents = document.querySelectorAll("[data-attach-chat-notification]")
chatNotificationParents.forEach(element => {
    chatNotificationCount(element)
})