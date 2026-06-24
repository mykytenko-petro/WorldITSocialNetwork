import { imageInput, removeImageButton } from "./chatComponents.js"

export const convertToBase64 = (file) => {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = (error) => reject(error);
    });
};

const imageDiv = document.getElementById("imagesPreview")
const MAX_IMAGES = 7

export const openFile = async () => {
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

            console.log(imageDiv)

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