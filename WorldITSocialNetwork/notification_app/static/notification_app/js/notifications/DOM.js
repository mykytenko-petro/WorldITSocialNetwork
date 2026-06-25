import { chatNotificationCount } from "./components.js"

export function formatCount(count) {
    if (Number(count) > 9) {
        return "9+"
    }

    if (count == 0) {
        return ''
    }

    return count
}

// assign notifications
const chatIcon = document.querySelector("#chat-icon")
chatNotificationCount("total", chatIcon)

const personalChatIcon = document.querySelector("#personal-chat-icon")
if (personalChatIcon) {
    chatNotificationCount("personal", personalChatIcon)
}

const groupChatIcon = document.querySelector("#group-chat-icon")
if (groupChatIcon) {
    chatNotificationCount("group", groupChatIcon)
}