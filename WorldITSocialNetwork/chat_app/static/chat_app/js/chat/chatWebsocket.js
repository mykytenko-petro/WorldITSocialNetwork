let chatSocket

document.addEventListener("ws:openChat", (e) => {
    const { chatId } = e.detail

    if (chatSocket) {
        chatSocket.close()
    }

    chatSocket = new WebSocket(`ws://${window.location.host}/chat/${chatId}/`)
    chatSocket.onmessage = (e) => recieveMessage(e)
})

// TODO: add images
document.addEventListener("ws:sendMessage", (e) => {
    const { data } = e.detail

    chatSocket.send(JSON.stringify(data))
})

function recieveMessage(event) {
    const data = JSON.parse(event.data)

    // console.log(data)

    if (data.id) {
        document.dispatchEvent(new CustomEvent("dom:openChat", {
            detail: {
                chatId: data.id
            }
        }))
    }

    switch (data.type) {
        case "send_message":
            document.dispatchEvent(new CustomEvent("dom:insertMessage", {
                detail: {
                    html: data.html
                }
            }))
    }
}