import { PaginationProvider } from "/static/js/utils/paginationProvider.js"
import { contactProviderUrl } from "./contactsAPI.js"

export const contactConteiner = document.querySelector('.contact-container')

new PaginationProvider(
    contactProviderUrl,
    contactConteiner
)