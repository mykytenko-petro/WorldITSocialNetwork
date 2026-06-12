import { PaginationProvider } from "/static/js/utils/paginationProvider.js"
import { renderHTML } from "/static/js/utils/renderHTML.js"

const groupChatContainer = document.querySelector("#groupChats")

// TODO: make image
const chatCard = (data) => {
    const { 
        chat_id: chatId,
        timestamp,
        name,
        time,
        message_text: messageText
    } = data

    return renderHTML(/* html */ `
        <div class="chat-card" data-chat-id="${chatId}" data-timestamp="${timestamp}">
            <img src="/static/chat_app/icon/Avatar.png" alt="">

            <div class="chat-card-content">
                <div class="chat-card-info">
                    <p class="chat-name">${name}</p>
                    <p class="chat-time">${time}</p>
                </div>

                <p>${messageText}</p>
            </div>
        </div>
    `)
}

class ChatCardPaginationProvider extends PaginationProvider {
    dataCallback(data) {
        for (const chatData of data.data) {
            groupChatContainer.appendChild(chatCard(chatData))
        }
    }
}

new ChatCardPaginationProvider(
    `/chat/group_chat_provider/`,
    groupChatContainer
)