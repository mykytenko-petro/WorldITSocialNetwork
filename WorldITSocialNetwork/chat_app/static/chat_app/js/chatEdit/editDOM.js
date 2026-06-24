export const newGroupModal = document.querySelector(".new-group-dialog")
const newGroupStep = document.querySelector('[data-step="members"]')
const detailsGroupStep = document.querySelector('[data-step="details"]')
const editGroupStep = document.querySelector('[data-step="edit"]')

const backGroup = document.querySelector(".new-group-back")
const saveButton = newGroupModal.querySelector("#new-group-next")
const threeDotButton = document.querySelector(".three-dot")
const participantAddButton = document.querySelector(".participant-add")

saveButton.addEventListener("click", (event) => {
    editGroupStep.style.display = "none"
    detailsGroupStep.style.display = "none"
    newGroupStep.style.display = "none"

})

backGroup.addEventListener("click", (event) => {
    detailsGroupStep.style.display = "none"
    newGroupStep.style.display = "none"
    editGroupStep.style.display = "none"
})

threeDotButton.addEventListener("click", (event) => {
    detailsGroupStep.style.display = "none"
    newGroupStep.style.display = "none"
    editGroupStep.style.display = "flex"
})

participantAddButton.addEventListener("click", (event) => {
    detailsGroupStep.style.display = "none"
    newGroupStep.style.display = "none"
    editGroupStep.style.display = "none"
})