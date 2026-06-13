// TODO: later move to cross app feature
const notificationWebsocket = new WebSocket(`ws://${window.location.host}/chat/notifications/`)

notificationWebsocket.onmessage = (e) => {
    const data = JSON.parse(e.data)
    console.log(data)
}