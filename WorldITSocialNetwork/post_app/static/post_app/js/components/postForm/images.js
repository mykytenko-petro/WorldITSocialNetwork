import { postForm } from "./form.js"

// dom
const imageDiv = postForm.querySelector("#images")
const createImageButton = postForm.querySelector("#createImage")

// components
const imageInput = (file) => {
    const div = document.createElement("div")

    const img = document.createElement("img")
    img.src = URL.createObjectURL(file)

    const input = document.createElement("input")
    input.type = "file"
    input.name = "images"
    input.style.display = "none"

    // Use DataTransfer to programmatically bypass the security restriction 
    // that usually prevents manual assignment of files to an input element
    const dataTransfer = new DataTransfer()
    dataTransfer.items.add(file)
    input.files = dataTransfer.files

    const removeBtn = removeImageButton(div, img.src)

    div.appendChild(img)
    div.appendChild(input)
    div.appendChild(removeBtn)

    return div
}

const removeImageButton = (parentToElement, objectUrl) => {
    const button = document.createElement("button")

    const icon = document.createElement("img")
    icon.src = "/static/post_app/icon/trash.png";
    button.appendChild(icon)

    button.addEventListener("click", () => {
        parentToElement.remove()
        // Release the memory used by the preview image to prevent memory leaks
        URL.revokeObjectURL(objectUrl)
    })

    return button
}

// logic
const openFile = async () => {
    try {
        // Launch the system file picker via the File System Access API
        const [fileHandle] = await window.showOpenFilePicker({
            types: [{
                description: "Images",
                accept: { "image/*": [".png", ".gif", ".jpeg", ".jpg", ".webp"] }
            }],
            excludeAcceptAllOption: true,
            multiple: false,
        })

        // Convert the file handle provided by the system into a standard File object
        const file = await fileHandle.getFile()
        
        // Build the component and inject it into the image container
        const newImageEntry = imageInput(file)
        imageDiv.appendChild(newImageEntry)

    } catch (err) {
        if (err.name !== 'AbortError') {
            console.error("Picker error:", err)
        }
    }
}

createImageButton.addEventListener("click", openFile)