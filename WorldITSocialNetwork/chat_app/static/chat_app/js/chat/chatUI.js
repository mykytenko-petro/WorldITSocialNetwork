const sendMessageForm = document.querySelector(".chat-form")

sendMessageForm.addEventListener("submit", (event) => {
    event.preventDefault()
    const data = Object.fromEntries(new FormData(sendMessageForm).entries())

    sendMessageForm.querySelector("input").value = ""

    document.dispatchEvent(new CustomEvent("ws:sendMessage", {
        detail: {
            data: data
        }
    }))
})