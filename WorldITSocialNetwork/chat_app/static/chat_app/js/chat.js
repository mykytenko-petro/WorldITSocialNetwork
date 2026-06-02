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
}