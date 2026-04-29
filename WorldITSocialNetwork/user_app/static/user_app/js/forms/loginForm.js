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

        alert("redirect")
    }
)