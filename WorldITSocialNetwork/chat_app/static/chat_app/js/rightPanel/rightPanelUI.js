const groupChatContainer = document.querySelector("#groupChats")



groupChatContainer.addEventListener("click", (event) => {
    const element = event.target

    if (!element.closest("[data-chat-id]")) {
        return
    }

    const parentElement = element.closest("[data-chat-id]")
    
    document.dispatchEvent(new CustomEvent("ws:openChat", {
        detail: {
            chatId: parentElement.dataset.chatId
        }
    }))
})