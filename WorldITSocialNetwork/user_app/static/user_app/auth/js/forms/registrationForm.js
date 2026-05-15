import { showForm } from "../displayLogic.js"
import { registerForm, loginButton } from "../DOM.js"

loginButton.addEventListener("click", () => {
    showForm("loginForm")
})

registerForm.addEventListener(
    'submit', 
    function(event){
        event.preventDefault()
        const form = event.target
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
            
            Cookies.set("currentEmail", data.email, { expires: 7 })
            showForm('confirmEmailForm')
        })
        .catch(async (errors) => {
            alert(JSON.stringify(errors))
        })
    }
)