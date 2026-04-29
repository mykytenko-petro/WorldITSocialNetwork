export const loginForm = document.getElementById("login-form-container")
export const registerForm = document.getElementById("register-form-container")
export const confirmEmailForm = document.getElementById("confirm-email-form-container")


loginForm.style.display = "none"
registerForm.style.display = "none"
confirmEmailForm.style.display = "none"

export const CSRF_token = Cookies.get('csrftoken')


export function showForm(formName){
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

