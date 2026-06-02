export const contactConteiner = document.querySelector('.contact-container')

const greetingScreen = document.querySelector("#greetingScreen")
const openedChat = document.querySelector("#openedChat")

export const sendMessageButton = document.querySelector("#sendMessage")
export const messageContainer = document.querySelector(".messanger")

// visibility handling
export function openChat() {
    greetingScreen.style.display = "none"
    openedChat.style.display = "flex"
}