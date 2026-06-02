import { sendMessage } from "./chat.js"
import { sendMessageButton } from "./DOM.js"

sendMessageButton.addEventListener("click", (event) => {
    const form = event.currentTarget.closest("form")
    const data = Object.fromEntries(new FormData(form).entries())

    sendMessage(data)
})