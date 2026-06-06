import { PaginationProvider } from "/static/js/utils/paginationProvider.js"

const greetingScreen = document.querySelector("#greetingScreen")
const openedChat = document.querySelector("#openedChat")
const chatContainer = document.querySelector(".chat-container")
const chatNameP = document.querySelector(".name-chat .big")

// TODO: add name of chat
document.addEventListener("dom:openChat", (e) => {
    const { chatId, chatName } = e.detail

    greetingScreen.style.display = "none"
    openedChat.style.display = "flex"

    chatContainer.innerHTML = ""

    chatNameP.textContent = chatName

    new PaginationProvider(
        `/chat/messages/${chatId}`,
        chatContainer,
    )
})

document.addEventListener("dom:insertMessage", (e) => {
    const { html } = e.detail

    chatContainer.insertAdjacentHTML("afterbegin", html)
})