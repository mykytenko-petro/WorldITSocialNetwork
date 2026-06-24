document.addEventListener("api:sendCreateGroupChat", (e) => {
    fetch(
        "/chat/create_group_chat/",
        {
            method: "POST",
            headers: {
                "X-CSRFToken": CSRFToken
            },
            body: e.detail.formData
        }
    )
        .then(response => {
            if (!response.ok) {
                console.error(response.status)
                return
            }

            return response
        })
        .then(response => response.json())
        .then(response => {
            document.dispatchEvent(new CustomEvent("ui:openGroupChat", {
                detail: {
                    chatId: response.chat_id
                }
            }))
        })
})