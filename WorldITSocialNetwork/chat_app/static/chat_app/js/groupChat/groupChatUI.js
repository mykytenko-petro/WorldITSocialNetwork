import { newGroupModal } from "./groupChatDOM.js"

const cancelButton = document.querySelector("#cancel")
const formMembers = document.querySelector("[data-step='members']")

cancelButton.addEventListener("click", () => {
    formMembers.reset()

    newGroupModal.close()
})