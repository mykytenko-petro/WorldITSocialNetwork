import { lastChatId } from "./chatWebsocket.js"

document.addEventListener("api:getChatId", (e) => {
    const { userId } = e.detail

    fetch(`/chat/chat_with/${userId}/`, {
        method: 'POST',
        headers: {
            "X-CSRFToken": CSRFToken
        },
    })
        .then(response => {
            if (!response.ok) {
                console.error(response.status)
                return
            }

            return response
        })
        .then(response => response.json())
        .then(data => {
            document.dispatchEvent(new CustomEvent("ws:openChat", {
                detail: {
                    chatId: data.chat_id
                }
            }))
        })
})

document.addEventListener("api:openChat", (e) => {
    const { chatId } = e.detail

    fetch(`/chat/get_chat_info/${chatId}/`)
        .then(response => {
            if (!response.ok) {
                console.error(response.status)
                return
            }
    
            return response
        })
        .then(response => response.json())
        .then(data => {
            document.dispatchEvent(new CustomEvent("dom:openChat", {
                detail: {
                    ...data
                }
            }))
        })
})

document.addEventListener("api:sendMessage", (e) => {
    const { data } = e.detail

    console.log(data)

    fetch(`/chat/save_message/${lastChatId}/`, {
        method: 'POST',
        headers: {
            "X-CSRFToken": CSRFToken
        },
        body: data
    })
        // .then(response => {
        //     if (!response.ok) {
        //         console.error(response.status)
        //         return
        //     }

        //     return response
        // })
        // .then(response => response.json())
        // .then(data => {
        //     document.dispatchEvent(new CustomEvent("ws:openChat", {
        //         detail: {
        //             chatId: data.chat_id
        //         }
        //     }))
        // })
})