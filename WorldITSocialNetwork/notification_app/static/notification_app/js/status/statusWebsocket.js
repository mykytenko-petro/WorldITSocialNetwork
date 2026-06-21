import { socket } from "/static/js/features/websocket.js"

setInterval(() => {
    const statusBubbles = document.querySelectorAll(".status-bubble")
    const userIds = Array.from(statusBubbles).map(element => {
        return element.dataset.userId
    })

    socket.emit(
        "getUsersOnline",
        { userIds },
        response => {
            statusBubbles.forEach(element => {
                if (response.onlineUserIds.includes(element.dataset.userId)) {
                    element.classList.add("online")
                } else {
                    element.classList.remove("online")
                }
            })
        }
    )
}, 1000)