import {showForm, CSRF_token, loginForm, registerForm, confirmEmailForm}  from "./authforms.js";

const registerButton = document.getElementById("open-register-form")
const loginButton = document.getElementById("open-login-form")
const confirmEmailButton = document.getElementById("button-confirm")
const backEmailButton = document.getElementById("button-back")

registerButton.addEventListener("click", () => {
    showForm("registerForm")
})

loginButton.addEventListener("click", () => {
    showForm("loginForm")
})

confirmEmailButton.addEventListener("click", (event) => {
    event.preventDefault()
    showForm("confirmEmailForm")
})

backEmailButton.addEventListener("click", () => {
    showForm("registerForm")
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
                'X-CSRFToken': CSRF_token,
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: formData
        })
        .then(async response =>{
            const data = await response.json()
            if (!response.ok){
                throw data
            }
            showForm('confirmEmailForm')
        })
    }
)