
const FORM_IDS = {
    login: "login-form-container",
    register: "register-form-container",
    confirm: "confirm-email-form-container",
}

const COOKIE_NAME = "auth_form_state"
const VALID_STATES = Object.keys(FORM_IDS)


function getCookie(name){
    const cookies = document.cookie.split(';')
    for (const cookie of cookies){
        const trimmed = cookie.trim()
        if (trimmed.startsWith(`${name}=`))
    return trimmed.substring(name.length + 1)}
}
function hideAllForms() {
    const loginForm = document.getElementById("login-form-container")
    const registerForm = document.getElementById("register-form-container")
    const confirmForm = document.getElementById("confirm-email-form-container")

    if(loginForm){
        loginForm.style.display = "none"
    }
    if(registerForm){
        registerForm.style.display = "none"
    }
    if(confirmForm){
        confirmForm.style.display = "none"
    }
}
hideAllForms()


function showForm(formName){
    hideAllForms()
    if (formName === "login"){
        const form = document.getElementById("login-form-container")
        if (form){form.style.display = "block"}
    }
    if (formName === "register"){
        const form = document.getElementById("register-form-container")
        if (form){form.style.display = "block"}
    }
    if (formName === "confirm"){
        const form = document.getElementById("confirm-email-form-container")
        if (form){form.style.display = "block"}
    }
}
const openLogin = document.getElementById("open-login-form")
const openRegister = document.getElementById("open-register-form")


openLogin.addEventListener("click", () => {showForm("login")})
openRegister.addEventListener("click", () => {console.log(123)})
// showForm("register")
