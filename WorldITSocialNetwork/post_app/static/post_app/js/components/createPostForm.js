const buttonCreatePost = document.querySelector("#create-post button")

const postForm = document.getElementById("create-post-form")
const sendButton = postForm.querySelector("#create-post-form #send")

buttonCreatePost.addEventListener("click", () => {
    const textarea = document.querySelector("#create-post textarea")

    postForm.showModal()

    const textareaForm = postForm.querySelector("textarea")
    textareaForm.value = textarea.value
})

sendButton.addEventListener("click", () => {
    const form = postForm.querySelector("form")
    const formData = new FormData(form)

    fetch(form.action, {
        method : 'POST',
        headers: {
            'X-CSRFToken': CSRFToken,
            'X-Requested-With': 'XMLHttpRequest'
        },
        body: formData
    })
    .then(async response =>{
        const data = await response.json()
        if (!response.ok){
            throw data
        }
        

    })
    .catch(async (errors) => {
        alert(JSON.stringify(errors))
    })
})