import { contactCard, paginationThreshold } from "../contacts/contactsDOM.js"

const newGroupModal = document.querySelector(".new-group-dialog")

const createGroupButton = document.querySelector(".create-group-chat")
const createGroupCloseButton = document.querySelector(".new-group-close")

const contactContainer = newGroupModal.querySelector(".new-group-list")

createGroupButton.addEventListener("click", (event) => {
    newGroupModal.showModal()
})

createGroupCloseButton.addEventListener("click", (event) => {
    newGroupModal.close()
})

document.addEventListener("dom:pasteFilteredContacts", (e) => {
    const { data } = e.detail

    renderContacts(data)
})

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

    const thresholdElement = contactContainer.querySelector('hr')

    contactContainer.insertBefore(fragment, thresholdElement)

    contactContainer.scrollBy({
        top: -10,
        behavior: 'smooth'
    })
}

contactContainer.appendChild(paginationThreshold())