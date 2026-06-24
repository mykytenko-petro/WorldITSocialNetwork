import { formatCount } from "./DOM.js"
import { socket } from "/static/js/features/websocket.js"

socket.on("unreadCountUpdate", (data) => {
    const { summary, byChat } = data
    
    console.log(summary)

    const sumOfNotificationsCount = document.querySelector('.notification-count[data-role="total"]')
    sumOfNotificationsCount.textContent = formatCount(summary.total)

    const personalNotificationsCount = document.querySelector('.notification-count[data-role="personal"]')
    personalNotificationsCount.textContent = formatCount(summary.personal)

    const groupNotificationsCount = document.querySelector('.notification-count[data-role="group"]')
    groupNotificationsCount.textContent = formatCount(summary.group)
})