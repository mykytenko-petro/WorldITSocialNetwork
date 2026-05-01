import { confirmEmailForm, loginForm, registerForm } from "./DOM.js"

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

        const description = document.querySelector("#description")
        const email = Cookies.get("currentEmail")
        description.textContent = `Ми надіслали 6-значний код на вашу пошту (${email}). Введіть його нижче, щоб підтвердити акаунт`
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