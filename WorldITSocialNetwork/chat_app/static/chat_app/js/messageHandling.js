import { PaginationProvider } from "/static/js/utils/paginationProvider.js"
import { sendMessage } from "./chat.js"
import { messageContainer, sendMessageButton } from "./DOM.js"

sendMessageButton.addEventListener("click", (event) => {
    const form = event.currentTarget.closest("form")
    const data = Object.fromEntries(new FormData(form).entries())

    sendMessage(data)
})

export function loadMessages() {
    new PaginationProvider(
        `/chat/messages/${messageContainer.dataset.chatId}`,
        messageContainer,
        null,
        null,
        true
    )
}