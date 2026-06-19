import { socket } from "/static/js/features/websocket.js"

export let lastChatId
const pseudonym = document.querySelector('meta[name="pseudonym"]').getAttribute('content')

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

document.addEventListener("ws:sendMessage", (e) => {
    const { data } = e.detail

    const objectData = Object.fromEntries(data)

    socket.emit(
        "sendMessage",
        {
            chat_id: lastChatId,
            pseudonym: pseudonym,
            avatar: "",
            ...objectData
        },
        () => {
            console.log(2232)
        }
    )
})
