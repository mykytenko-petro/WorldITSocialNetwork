const loginForm = document.getElementById("login-form-container")
const registerForm = document.getElementById("register-form-container")
const confirmEmailForm = document.getElementById("confirm-email-form-container")

const registerButton = document.getElementById("open-register-form")
const loginButton = document.getElementById("open-login-form")
const confirmEmailButton = document.getElementById("button-confirm")
const backEmailButton = document.getElementById("button-back")

loginForm.style.display = "none"
registerForm.style.display = "none"
confirmEmailForm.style.display = "none"

function showForm(formName){
    if(formName === "loginForm"){
        loginForm.style.display = "flex"
        registerForm.style.display = "none"
        confirmEmailForm.style.display = "none"
    }
    else if(formName === "confirmEmailForm"){
        confirmEmailForm.style.display = "flex"
        loginForm.style.display = "none"
        registerForm.style.display = "none"
    }
    else if(formName === "registerForm"){
        registerForm.style.display = "flex"
        loginForm.style.display = "none"
        confirmEmailForm.style.display = "none"
    }
    Cookies.set('lastForm', formName, { expires: 7 })
}

const savedForm = Cookies.get('lastForm') || 'registerForm'
showForm(savedForm)

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