import { contactCard, paginationThreshold } from "../contacts/contactsDOM.js"

export const newGroupModal = document.querySelector(".new-group-dialog")
const newGroupStep = document.querySelector('[data-step="members"]')
const detailsGroupStep = document.querySelector('[data-step="details"]')
const backGroup = document.querySelector(".new-group-back")

const createGroupButton = document.querySelector(".create-group-chat")
const createGroupCloseButton = document.querySelector(".new-group-close")
const nextButton = newGroupModal.querySelector("#new-group-next")

const contactContainer = newGroupModal.querySelector(".new-group-list")
const chosenContactsContainer = newGroupModal.querySelector(".new-group-participants")

// Modal toggle events
createGroupButton.addEventListener("click", (event) => {
    newGroupModal.showModal()
})

createGroupCloseButton.addEventListener("click", (event) => {
    newGroupModal.close()
})

// Step navigation events
nextButton.addEventListener("click", (event) => {
    const inputs = Array.from(contactContainer.querySelectorAll("input:checked"))

    if (inputs.length < 2) {
        return
    }

    detailsGroupStep.style.display = "flex"
    newGroupStep.style.display = "none"

    renderChosenContacts()
})

backGroup.addEventListener("click", (event) => {
    detailsGroupStep.style.display = "none"
    newGroupStep.style.display = "flex"
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

// Custom DOM events
document.addEventListener("dom:pasteFilteredContacts", (e) => {
    const { data } = e.detail
    renderContacts(data)
})

// Render functions
export function renderContacts(groupedData) {
    const oldSections = contactContainer.querySelectorAll(".contact-letter-section")
    oldSections.forEach(section => section.remove())

    const fragment = document.createDocumentFragment()

    for (const [letter, contactsArray] of groupedData) {
        const contactSection = document.createElement("div")
        contactSection.className = "contact-letter-section"

        const letterHeader = document.createElement("p")
        letterHeader.className = "new-group-letter"
        letterHeader.textContent = letter
        contactSection.appendChild(letterHeader)

        contactsArray.forEach(contact => {
            const contactWrapper = document.createElement("div")
            contactWrapper.className = "contact-wrapper"
            contactWrapper.appendChild(contactCard(contact, "select"))
            contactSection.appendChild(contactWrapper)
        })

        fragment.appendChild(contactSection)
    }

    const thresholdElement = contactContainer.querySelector("hr")
    contactContainer.insertBefore(fragment, thresholdElement)

    contactContainer.scrollBy({
        top: -10,
        behavior: "smooth"
    })
}

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

contactContainer.appendChild(paginationThreshold())