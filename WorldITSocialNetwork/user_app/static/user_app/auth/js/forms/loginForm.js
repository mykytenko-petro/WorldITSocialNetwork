import { showForm } from "../displayLogic.js"
import { loginForm, registerButton } from "../DOM.js"

registerButton.addEventListener("click", () => {
    showForm("registerForm")
})

loginForm.addEventListener("submit", 
    function(event) {
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
            
            window.location.href = "/"
        })
        .catch(async (errors) => {
            alert(JSON.stringify(errors))
        })
    }
)