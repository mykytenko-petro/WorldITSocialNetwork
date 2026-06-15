let chatSocket
export let lastChatId

document.addEventListener("ws:openChat", (e) => {
    const { chatId } = e.detail

    if (lastChatId === chatId) {
        return
    }

    lastChatId = chatId

    if (chatSocket) {
        chatSocket.close()
    }

    chatSocket = new WebSocket(`ws://${window.location.host}/chat/${chatId}/`)
    chatSocket.onmessage = (e) => recieveMessage(e)
})

function recieveMessage(event) {
    const data = JSON.parse(event.data)

    switch (data.type) {
        case "handshake":
            document.dispatchEvent(new CustomEvent("dom:openChat", {
                detail: {
                    chatId: data.chat_id,
                    chatName: data.chat_name
                }
            }))
            break;
        case "send_message":
            document.dispatchEvent(new CustomEvent("dom:insertMessage", {
                detail: {
                    html: data.html
                }
            }))
            break;
    }
}