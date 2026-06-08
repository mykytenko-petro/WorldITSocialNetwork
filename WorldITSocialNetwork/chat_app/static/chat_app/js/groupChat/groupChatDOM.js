const newGroupModal = document.querySelector(".new-group-dialog")

const createGroupButton = document.querySelector(".create-group-chat")
const createGroupCloseButton = document.querySelector(".new-group-close")

const contactContainer = newGroupModal.querySelector(".new-group-list")

createGroupButton.addEventListener("click", (event) => {
    newGroupModal.showModal()

    if (contactContainer.innerHTML === "") {
        document.dispatchEvent(new CustomEvent("api:getSortedContacts"))
    }
})

createGroupCloseButton.addEventListener("click", (event) => {
    newGroupModal.close()
})

document.addEventListener("dom:pasteFilteredContacts", (e) => {
    const { html } = e.detail

    contactContainer.innerHTML = html
})
// const membersStep = document.querySelector('[data-step="members"]')
// const detailsStep = document.querySelector('[data-step="details"]')
// const nextButton = document.querySelector(".new-group-next")
// const backButton = document.querySelector(".new-group-back")

// const showStep = (stepName) => {
//     membersStep.classList.toggle("is-active", stepName === "members")
//     detailsStep.classList.toggle("is-active", stepName === "details")
// }

// nextButton.addEventListener("click", () => showStep("details"))
// backButton.addEventListener("click", () => showStep("members"))
