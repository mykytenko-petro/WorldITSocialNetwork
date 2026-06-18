const WebsocketBackendURL = "http://192.168.0.121:8000"
// const WebsocketBackendURL = "https://yu-unabiding-vampishly.ngrok-free.dev"

async function getToken() {
    const res = await fetch("/socket_token/", {
        method: "GET",
    })

    const data = await res.json();
    return data.token;
}

const token = await getToken()

export const socket = io(WebsocketBackendURL, {
    autoConnect: false,
    auth: {
        token: `Bearer ${token}`,
    },
    extraHeaders: {
        "ngrok-skip-browser-warning": "any-value"
    }
})

socket.on("connect", () => {
    console.log("✅ Connected successfully!")
})

socket.on("connect_error", (err) => {
    console.log("❌ connect_error:", err.message)
})

socket.on("disconnect", (reason) => {
    console.log("🔌 Disconnected:", reason)
})

socket.connect()