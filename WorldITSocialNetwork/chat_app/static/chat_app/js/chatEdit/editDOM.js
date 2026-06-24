export const newGroupModal = document.querySelector(".new-group-dialog")
const newGroupStep = document.querySelector('[data-step="members"]')
const detailsGroupStep = document.querySelector('[data-step="details"]')
const editGroupStep = document.querySelector('[data-step="edit"]')
const addUserGroupStep = document.querySelector('[data-step="participant-adding"]')

const backGroup = document.querySelector(".new-group-back")
const saveButton = newGroupModal.querySelector("#new-group-next")
const threeDotButton = document.querySelector(".three-dot")
const participantAddButton = document.querySelector(".participant-add")

const contactContainer = newGroupModal.querySelector(".new-group-list")
const chosenContactsContainer = newGroupModal.querySelector(".new-group-participants")

saveButton.addEventListener("click", (event) => {
    editGroupStep.style.display = "none"
    detailsGroupStep.style.display = "none"
    newGroupStep.style.display = "none"
    addUserGroupStep.style.display = "none"

})

backGroup.addEventListener("click", (event) => {
    detailsGroupStep.style.display = "none"
    newGroupStep.style.display = "none"
    editGroupStep.style.display = "none"
    addUserGroupStep.style.display = "none"
})

threeDotButton.addEventListener("click", (event) => {
    detailsGroupStep.style.display = "none"
    newGroupStep.style.display = "none"
    editGroupStep.style.display = "flex"
    addUserGroupStep.style.display = "none"
})

participantAddButton.addEventListener("click", (event) => {
    detailsGroupStep.style.display = "none"
    newGroupStep.style.display = "none"
    editGroupStep.style.display = "none"
    addUserGroupStep.style.display = "flex"
})

chosenContactsContainer.addEventListener("click", (event) => {
    const element = event.target

    console.log(element)

    if (!(element.parentElement.matches("button") || element.matches("button"))) {
        return
    }

    const card = element.closest("[data-user-id]")
    const userId = card.dataset.userId
    const input = contactContainer.querySelector(`[data-user-id='${userId}'] input`)
    input.checked = false
    card.remove()
})

function renderChosenContacts() {
    const inputs = Array.from(contactContainer.querySelectorAll("input:checked"))
    const cards = inputs.map(input => input.closest(".contact").cloneNode(true))
    cards.forEach(card => {
        const checkbox = card.querySelector("input")
        checkbox.outerHTML = /* html */ `
            <button class="button" type="button">
                <img src="${'/static/icon/bin.svg'}">
            </button>
        `
    })

    chosenContactsContainer.innerHTML = ""
    chosenContactsContainer.append(...cards)
}