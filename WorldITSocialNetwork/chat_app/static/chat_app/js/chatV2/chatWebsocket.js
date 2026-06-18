import { socket } from "/static/js/features/websocket.js"

export let lastChatId

document.addEventListener("ws:openChat", (e) => {
    const { chatId } = e.detail

    if (lastChatId === chatId) {
        return
    }

    lastChatId = chatId

    // console.log(2232)

    socket.emit(
        "joinChat",
        { chatId: chatId },
        () => {
            console.log(chatId)
            document.dispatchEvent(new CustomEvent("api:openChat", { detail: {
                chatId: chatId
            }}))
        }
    )
})


/*
        const listener = (newMessage: IMessage) => {
        if (newMessage.chat_id === chatId) {
            updateCachedData((draft) => {
                draft.messages.unshift(newMessage);
            })
        }
    }

    socket.on("newMessage", listener)
*/