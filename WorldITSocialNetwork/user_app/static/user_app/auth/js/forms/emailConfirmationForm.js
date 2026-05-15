import { showForm } from "../displayLogic.js"
import { backEmailButton, confirmEmailForm, confirmEmailFormButton } from "../DOM.js"

backEmailButton.addEventListener("click", () => {
    showForm("registerForm")
})

confirmEmailFormButton.addEventListener("click", 
    function(event) {
        const form = confirmEmailForm.querySelector("form")
        const formData = new FormData(form)

        formData.set("email", Cookies.get("currentEmail"))

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
            
            showForm("loginForm")
        })
        .catch(async (errors) => {
            alert(JSON.stringify(errors))
        })
    }
)
