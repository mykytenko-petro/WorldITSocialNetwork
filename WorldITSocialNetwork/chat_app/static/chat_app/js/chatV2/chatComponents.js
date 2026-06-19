import { renderHTML } from "/static/js/utils/renderHTML.js"

export const imageInput = (file) => {
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

export const removeImageButton = (parentElement, objectUrl) => {
    const button = document.createElement("button")
    const img = document.createElement("img")
    button.type = "button"
    button.classList.add("delete-image")

    button.appendChild(img)
    img.src = "/static/post_app/icon/trash.png"

    button.addEventListener("click", () => {
        parentElement.remove()
        URL.revokeObjectURL(objectUrl)
    })

    return button
}

export const messageCard = (data) => {
    const {
        sender_id: senderId,
        text,
        user_app_user,
        chat_app_messageimage: images
    } = data

    const userId = document.querySelector('meta[name="userId"]').getAttribute('content')

    const isMine = (userId == senderId)
    console.log(isMine)
    
    return renderHTML(/* html */`
        <div class="message-container ${isMine ? `my` : ''}">
            <div class="message">
                ${!isMine
                    ? `<img src="${MediaURL + user_app_user.profile_app_profile.avatar || '/static/chat_app/icon/Avatar.png'}" alt="Avatar">`
                    : ''
                }

                <div class="message-content-container ${isMine ? `my` : ''}">
                    <div class="message-text">
                        ${!isMine ? `<p>${user_app_user.profile_app_profile.pseudonym}</p>` : ''}

                        ${text ? `<p class="message-text-content">${text}</p>` : ''}
                        
                        ${images && images.length ? images.map(img => `
                            <img src="${MediaURL + img.image}" alt="Message attachment">
                        `).join('') : ''}
                    </div>
                    <div class="message-info">
                        <!-- <p>{{ message.time }}</p> -->
                        <img src="/static/chat_app/icon/mark.svg">
                    </div>
                </div>
            </div>
        </div>
    `)
}