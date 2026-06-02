import { messageContainer } from "./DOM.js"
import { loadMessages } from "./messageHandling.js"

let chatSocket

export function connectToChat(chatId) {
    if (chatSocket) {
        chatSocket.close()
    }

    chatSocket = new WebSocket(`ws://${window.location.host}/chat/${chatId}/`)
    chatSocket.onmessage = (event) => recieveMessage(event)
}

export function sendMessage(data) {
    chatSocket.send(JSON.stringify(data))
}

function recieveMessage(event) {
    const data = JSON.parse(event.data)

    console.log(data)

    if (data.id) {
        console.log(data.id)
        messageContainer.dataset.chatId = data.id
        loadMessages()
    }

    switch (data.type) {
        case "send_message":
            messageContainer.innerHTML += data.html
    }
}