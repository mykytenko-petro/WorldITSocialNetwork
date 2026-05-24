// dom
export const postForm = document.getElementById("create-post-form")

const sendButton = postForm.querySelector("#send")
const closeButton = postForm.querySelector("#close")

// logic
closeButton.addEventListener("click", () => {
    postForm.close()
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
        
        postForm.close()
    })
    .catch(async (errors) => {
        alert(JSON.stringify(errors))
    })
})