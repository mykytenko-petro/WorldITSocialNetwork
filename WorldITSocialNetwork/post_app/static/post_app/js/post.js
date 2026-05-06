const postForm = document.getElementById("create-post-form")
const buttonCreatePost = document.querySelector("#create-post button")

const closeButton = postForm.querySelector("#create-post-form > div > button")

buttonCreatePost.addEventListener("click", () => {
    const textarea = document.querySelector("#create-post textarea")

    postForm.showModal()

    const textareaForm = postForm.querySelector("textarea")
    console.log(textarea.textContent)
    textareaForm.value = textarea.value
})

// postForm.showModal()

closeButton.addEventListener("click", () => {
    postForm.close()
})