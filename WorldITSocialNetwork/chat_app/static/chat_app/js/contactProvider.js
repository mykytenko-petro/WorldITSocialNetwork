import { PaginationProvider } from "/static/js/utils/paginationProvider.js"
import { contactConteiner } from "./DOM.js"
import { connectToChat } from "./chat.js"

const contactProviderUrl = document.querySelector("meta[name='contactProviderUrl']").getAttribute("content")

new PaginationProvider(
    contactProviderUrl,
    contactConteiner
)

contactConteiner.addEventListener("click", (event) => {
    const element = event.target.closest("div")
    if (!element.matches("[data-user-id]")) {
        return
    }
    // TODO: make a check for same chat
    const url = `/chat/chat_with/${element.dataset.userId}/`

    fetch(url, {
        method: 'POST',
        headers: {
            "X-CSRFToken": CSRFToken
        },
    })
        .then(response => {
            if (!response.ok) {
                console.error(response.status)
                return
            }

            return response
        })
        .then(response => response.json())
        .then(data => {
            // TODO: add chat name
            
            connectToChat(data.chat_id)
        })
})