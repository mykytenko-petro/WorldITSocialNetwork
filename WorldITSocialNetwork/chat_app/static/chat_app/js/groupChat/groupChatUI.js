import { newGroupModal } from "./groupChatDOM.js"

const cancelButton = document.querySelector("#cancel")
const sendButton = document.querySelector("#new-group-create")

const formMembers = document.querySelector("[data-step='members']")
const formDetails = document.querySelector("[data-step='details']")

cancelButton.addEventListener("click", () => {
    formMembers.reset()
    formDetails.reset()

    newGroupModal.close()
})

sendButton.addEventListener("click", () => {
    const formData = new FormData(formDetails)

    document.dispatchEvent(new CustomEvent("api:sendCreateGroupChat", {detail: {
        formData: formData
    }}))
})

document.addEventListener("ui:openGroupChat", (e) => {
    const { chatId } = e.detail

    formMembers.reset()
    formDetails.reset()

    newGroupModal.close()

    document.dispatchEvent(new CustomEvent("ws:openChat", {
        detail: {
            chatId: chatId
        }
    }))
})

