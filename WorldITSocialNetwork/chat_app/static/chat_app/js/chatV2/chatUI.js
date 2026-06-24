const sendMessageForm = document.querySelector(".chat-form")
const imageContainer = sendMessageForm.querySelector("#imagesPreview")

sendMessageForm.addEventListener("submit", (event) => {
    event.preventDefault()
    const data = new FormData(sendMessageForm)

    sendMessageForm.reset()
    imageContainer.innerHTML = ""

    document.dispatchEvent(new CustomEvent("ws:sendMessage", {
        detail: {
            data: data
        }
    }))
})