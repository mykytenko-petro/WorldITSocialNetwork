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