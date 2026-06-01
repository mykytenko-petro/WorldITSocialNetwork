import { PaginationProvider } from "/static/js/utils/paginationProvider.js"
import { contactConteiner } from "./DOM.js"

const contactProviderUrl = document.querySelector("meta[name='contactProviderUrl']").getAttribute("contact");

new PaginationProvider(
    contactProviderUrl,
    contactConteiner
)

contactConteiner.addEventListener("click", (event) => {
    const element = event.target
    if(!element.matches("[data-user-id]")){
        return
    }
    console.log(element.dataset.userId)
})