import { postForm } from "./form.js"

// dom
export const createPostInput = document.getElementById("create-post-input")

const buttonCreatePost = createPostInput.querySelector("button")

// logic
buttonCreatePost.addEventListener("click", () => {
    const textarea = createPostInput.querySelector("textarea")

    postForm.showModal()

    const textareaForm = postForm.querySelector("textarea")
    textareaForm.value = textarea.value
})