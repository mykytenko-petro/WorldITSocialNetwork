import { statusBubble } from "/static/notification_app/js/status/statusComponents.js"
import { PaginationProvider } from "/static/js/utils/paginationProvider.js"
import { renderHTML } from "/static/js/utils/renderHTML.js"

const groupChatContainer = document.querySelector("#groupChats")
const messagesContainer = document.querySelector("#userChats")

// TODO: make image
export const chatCard = (data) => {
    const { 
        chat_id: chatId,
        name,
        time,
        message_text: messageText,
        chat_avatar_url: chatAvatarUrl,
        user_id: userId
    } = data

    const card = renderHTML(/* html */ `
        <div class="chat-card" data-chat-id="${chatId}">
            <img src="${chatAvatarUrl || "/static/chat_app/icon/Avatar.png"}" class="chat-avatar">

            <div class="chat-card-content">
                <div class="chat-card-info">
                    <p class="chat-name">${name}</p>
                    <p class="chat-time">${time}</p>
                </div>

                <p>${messageText}</p>
            </div>
        </div>
    `)

    if (userId) {
        const img = card.querySelector("img")
        statusBubble(img, userId)
    }

    return card
}

class ChatCardPaginationProvider extends PaginationProvider {
    dataCallback(data) {
        for (const chatData of data.data) {
            this.container.appendChild(chatCard(chatData))
        }
    }
}

new ChatCardPaginationProvider(
    `/chat/group_chat_provider/`,
    groupChatContainer
)

new ChatCardPaginationProvider(
    `/chat/message_chat_provider/`,
    messagesContainer
)

document.addEventListener("dom:updateChatCards", (e) => {
    const data = e.detail

    console.log(data)

    const oldChat = document.querySelector(`.chat-card[data-chat-id="${data.chat_id}"]`)

    if (oldChat) {
        oldChat.remove()
    }

    if (data.is_group) {
        groupChatContainer.insertAdjacentElement("afterbegin", chatCard(data))
    } else {
        messagesContainer.insertAdjacentElement("afterbegin", chatCard(data))
    }
})