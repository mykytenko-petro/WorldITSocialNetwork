import { contactConteiner } from "./contactsDOM.js"

contactConteiner.addEventListener("click", (event) => {
    const element = event.target.closest("div")
    if (!element.matches("[data-user-id]")) {
        return
    }

    document.dispatchEvent(new CustomEvent("apigetChatId:", {
        detail: {
            userId: element.dataset.userId
        }
    }))
})

