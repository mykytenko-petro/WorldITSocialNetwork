import { PaginationProvider } from "/static/js/utils/paginationProvider.js"

const greetingScreen = document.querySelector("#greetingScreen")
const openedChat = document.querySelector("#openedChat")
const chatContainer = document.querySelector(".chat-container")
const chatNameP = document.querySelector(".name-chat .big")

document.addEventListener("dom:openChat", (e) => {
    const { chatId, chatName } = e.detail

    greetingScreen.style.display = "none"
    openedChat.style.display = "flex"

    chatContainer.innerHTML = ""

    chatNameP.textContent = chatName

    new PaginationProvider(
        `/chat/messages/${chatId}`,
        chatContainer,
    )
})

document.addEventListener("dom:insertMessage", (e) => {
    const { html } = e.detail

    chatContainer.insertAdjacentHTML("afterbegin", html)
})

// images
const imageDiv = document.getElementById("imagePreview")
const imageButton = document.getElementById("imageButton")

const MAX_IMAGES = 7

const imageInput = (file) => {
    const wrapper = document.createElement("div")
    wrapper.classList.add("image-wrapper")

    const objectUrl = URL.createObjectURL(file)

    const img = document.createElement("img")
    img.src = objectUrl
    img.classList.add("preview-image")

    const input = document.createElement("input")
    input.type = "file"
    input.name = "images"
    input.hidden = true

    const dataTransfer = new DataTransfer()
    dataTransfer.items.add(file)
    input.files = dataTransfer.files

    const removeBtn = removeImageButton(wrapper, objectUrl)

    wrapper.appendChild(img)
    wrapper.appendChild(input)
    wrapper.appendChild(removeBtn)

    return wrapper
}

const removeImageButton = (parentElement, objectUrl) => {
    const button = document.createElement("button")
    button.type = "button"
    button.classList.add("delete-image")

    button.textContent = "✕"

    button.addEventListener("click", () => {
        parentElement.remove()
        URL.revokeObjectURL(objectUrl)
    })

    return button
}

const openFile = async () => {
    try {
        const currentImages = imageDiv.children.length

        if (currentImages >= MAX_IMAGES) {
            alert(`Maximum ${MAX_IMAGES} images allowed`)
            return
        }

        const fileHandles = await window.showOpenFilePicker({
            types: [{
                description: "Images",
                accept: {
                    "image/*": [
                        ".png",
                        ".jpg",
                        ".jpeg",
                        ".gif",
                        ".webp"
                    ]
                }
            }],
            excludeAcceptAllOption: true,
            multiple: true
        })

        const availableSlots = MAX_IMAGES - currentImages

        for (const handle of fileHandles.slice(0, availableSlots)) {
            const file = await handle.getFile()

            const image = imageInput(file)

            imageDiv.appendChild(image)
        }

        if (fileHandles.length > availableSlots) {
            alert(`Only ${MAX_IMAGES} images are allowed`)
        }

    } catch (err) {
        if (err.name !== "AbortError") {
            console.error(err)
        }
    }
}

imageButton.addEventListener("click", openFile)