import { contactConteiner } from "./contactsDOM.js"

let oldId

contactConteiner.addEventListener("click", (event) => {
    const element = event.target.closest("div")
    if (!element.matches("[data-user-id]")) {
        return
    }

    if (oldId === element.dataset.userId){
        return
    }
    
    document.dispatchEvent(new CustomEvent("api:getChatId", {
        detail: {
            userId: element.dataset.userId
        }
    }))
})

