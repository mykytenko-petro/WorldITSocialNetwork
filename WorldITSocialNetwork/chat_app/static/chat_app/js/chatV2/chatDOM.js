import { imageInput, messageCard, removeImageButton } from "./chatComponents.js"
import { openFile } from "./chatUtils.js"
import { PaginationProvider } from "/static/js/utils/paginationProvider.js"

const greetingScreen = document.querySelector("#greetingScreen")
const openedChat = document.querySelector("#openedChat")
const chatContainer = document.querySelector(".chat-container")
const chatNameP = document.querySelector(".name-chat .big")
const chatAvatar = document.querySelector(".chat-info-container img")

class MessagePaginationProvider extends PaginationProvider {
    dataCallback(data) {
        for (const messageData of data.data) {
            this.container.appendChild(messageCard(messageData))
        }
    }
}

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

    new MessagePaginationProvider(
        `/chat/messages/${chatId}`,
        chatContainer,
    )
})

document.addEventListener("dom:showMessage", (e) => {
    console.log(e.detail.data)

    chatContainer.insertAdjacentElement("afterbegin", messageCard(e.detail.data))
})

// images
const imageButton = document.getElementById("imageButton")

imageButton.addEventListener("click", openFile)