const sendMessageForm = document.querySelector(".chat-form")
const imageContainer = sendMessageForm.querySelector("#imagePreview")

sendMessageForm.addEventListener("submit", (event) => {
    event.preventDefault()
    const data = new FormData(sendMessageForm)

    sendMessageForm.reset()
    imageContainer.innerHTML = ""

    document.dispatchEvent(new CustomEvent("api:sendMessage", {
        detail: {
            data: data
        }
    }))
})