import { socket } from "/static/js/features/websocket.js"
import { convertToBase64 } from "./chatUtils.js"

export let lastChatId
const pseudonym = document.querySelector('meta[name="pseudonym"]').getAttribute('content')

document.addEventListener("ws:openChat", (e) => {
    const { chatId } = e.detail

    if (lastChatId === chatId) {
        return
    }

    if (lastChatId) {
        socket.emit(
            "leaveChat",
            { chatId: lastChatId },
        )
    }

    lastChatId = chatId

    socket.emit(
        "joinChat",
        { chatId: chatId },
        () => {
            document.dispatchEvent(new CustomEvent("api:openChat", { detail: {
                chatId: chatId
            }}))
        }
    )
})

document.addEventListener("ws:sendMessage", async (e) => {
    const { data } = e.detail;
    
    const objectData = Object.fromEntries(data);
    
    console.log(objectData)

    const allFiles = data.getAll('images');

    let base64ImageArray = [];

    const validFiles = allFiles.filter(file => file.size > 0);

    if (validFiles.length > 0) {
        try {
            base64ImageArray = await Promise.all(validFiles.map(file => convertToBase64(file)));
        } catch (error) {
            console.error("Failed to encode one or more images:", error);
            return;
        }
    }

    delete objectData['images'];

    console.log(base64ImageArray)

    socket.emit(
        "sendMessage",
        {
            chat_id: lastChatId,
            pseudonym: pseudonym,
            avatar: "",
            text: objectData["text"],
            photos: base64ImageArray
        },
        () => {
            console.log("Message with multiple Base64 images sent!");
        }
    );
});

socket.on(
    "newMessage",
    (data) => {
        console.log(data)

        if (data.chat_id != lastChatId) {
            console.log(data.chat_id, lastChatId)
            return
        }

        document.dispatchEvent(new CustomEvent("dom:showMessage", { detail: {
            data: data
        }}))
    }
)