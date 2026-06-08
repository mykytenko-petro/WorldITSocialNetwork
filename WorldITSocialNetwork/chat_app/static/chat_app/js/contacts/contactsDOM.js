import { getContactData } from "./contactsAPI.js"
import { filterContactsFlat } from "./contactsUtils.js"

export const contactConteiner = document.querySelector('.contact-container')

let page = 1
let isLoading = false

const cachedContacts = []

const parser = new DOMParser()
const contactCard = (data, mode) => {
    const { user_id: userId, pseudonym } = data

    let actionHtml = ''
    if (mode === "select") {
        actionHtml = `<input type="checkbox" class="button">`
    } else if (mode === "delete") {
        actionHtml = `
            <button class="button">
                <img src="${'/static/icon/bin.svg'}" alt="Delete">
            </button>`
    }

    const html = `
        <div class="contact" data-user-id="${userId}">
            <img src="${'/static/chat_app/icon/Avatar.png'}" alt="Avatar">
            <p>${pseudonym}</p>
            ${actionHtml}
        </div>
    `

    return parser.parseFromString(html, "text/html").body.firstChild
}

export const paginationThreshold = () => {
    const hr = document.createElement("hr")

    hr.style.opacity = "0"

    const observer = new IntersectionObserver(async (entries) => {
        if (entries[0].isIntersecting && !isLoading) {
            isLoading = true

            const data = await getContactData(page)

            if (data) {
                cachedContacts.push(...data.data)

                pasteContacts(cachedContacts)
                document.dispatchEvent(new CustomEvent("dom:pasteSortedContacts", {
                    detail: {
                        data: cachedContacts
                    }
                }))
            } else {
                observer.unobserve(hr)
                isLoading = false

                return
            }

            page++
            isLoading = false
            observer.unobserve(hr)
            setTimeout(() => { observer.observe(hr) }, 100)
        }
    }, { rootMargin: "200px" })
    observer.observe(hr)

    return hr
}

function pasteContacts(newData) {
    const sortedData = filterContactsFlat(newData)
    const threshold = contactConteiner.querySelector('hr')

    const existingCards = contactConteiner.querySelectorAll(`[data-user-id]`)

    sortedData.forEach((contact, index) => {
        const existingCard = existingCards[index]

        if (existingCard) {
            const nameElement = existingCard.querySelector('p')
            if (nameElement.textContent !== contact.pseudonym) {
                nameElement.textContent = contact.pseudonym
                existingCard.dataset.userId = contact.user_id
            }
        } else {
            const newCard = contactCard(contact)
            contactConteiner.insertBefore(newCard, threshold)
        }
    })



    contactConteiner.scrollBy({
        top: -10,
        behavior: 'smooth'
    })
}

contactConteiner.appendChild(paginationThreshold())