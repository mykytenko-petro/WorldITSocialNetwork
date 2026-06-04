import { PaginationProvider } from "/static/js/utils/paginationProvider.js"
import { sendMessage } from "./chat.js"
import { greetingScreen, messageContainer, openedChat, sendMessageForm } from "./DOM.js"

sendMessageForm.addEventListener("submit", (event) => {
    event.preventDefault()
    const form = event.currentTarget
    const data = Object.fromEntries(new FormData(form).entries())

    sendMessage(data)

    sendMessageForm.querySelector("input").value = ""
})

export function openChat(chatId) {
    greetingScreen.style.display = "none"
    openedChat.style.display = "flex"

    new PaginationProvider(
        `/chat/messages/${chatId}`,
        messageContainer,
        null,
        null,
        true
    )
}