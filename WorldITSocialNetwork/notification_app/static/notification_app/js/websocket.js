const notificationWebsocket = new WebSocket(`ws://${window.location.host}/notifications/`)

notificationWebsocket.onmessage = (e) => {
    const data = JSON.parse(e.data).data

    console.log(data)

    switch (data.type) {
        case "message_send":
            document.dispatchEvent(new CustomEvent("dom:updateChatCards", {
                detail: {
                    ...data
                }
            }))
            
            Cookies.set(
                "chatNotificationCount",
                Number(Cookies.get("chatNotificationCount") || 0) + 1
            )

            document.dispatchEvent(new CustomEvent("dom:updateChatNotificationCount"))
            break;
    }
}