import { PaginationProvider } from "/static/js/utils/paginationProvider.js"

const greetingScreen = document.querySelector("#greetingScreen")
const openedChat = document.querySelector("#openedChat")
const chatContainer = document.querySelector(".chat-container")
const chatNameP = document.querySelector(".name-chat .big")
const chatAvatar = document.querySelector(".chat-info-container img")

document.addEventListener("dom:openChat", (e) => {
    const {
        chat_id: chatId,
        chat_name: chatName,
        chat_avatar_url: chatAvatarUrl
    } = e.detail

    console.log(chatName)

    greetingScreen.style.display = "none"
    openedChat.style.display = "flex"

    chatContainer.innerHTML = ""
    chatNameP.textContent = chatName
    chatAvatar.src = chatAvatarUrl

    new PaginationProvider(
        `/chat/messages/${chatId}`,
        chatContainer,
    )
})

