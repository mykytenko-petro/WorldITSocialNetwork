import { showForm } from "../displayLogic.js"
import { backEmailButton, confirmEmailForm, confirmEmailFormButton } from "../DOM.js"

backEmailButton.addEventListener("click", () => {
    showForm("registerForm")
})

confirmEmailFormButton.addEventListener("click", 
    function(event) {
        const form = confirmEmailForm.querySelector("form")
        const formData = new FormData(form)

        showForm("loginForm")
    }
)
