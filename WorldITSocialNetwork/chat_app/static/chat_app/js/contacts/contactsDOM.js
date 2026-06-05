import { PaginationProvider } from "/static/js/utils/paginationProvider.js"
import { contactProviderUrl } from "./contactsAPI.js"

const contactConteiner = document.querySelector('.contact-container')

contactConteiner.addEventListener("click", (event) => {
    const element = event.target.closest("div")
    if (!element.matches("[data-user-id]")) {
        return
    }

    document.dispatchEvent(new CustomEvent("api:getChatId", {
        detail: {
            userId: element.dataset.userId
        }
    }))
})

new PaginationProvider(
    contactProviderUrl,
    contactConteiner
)