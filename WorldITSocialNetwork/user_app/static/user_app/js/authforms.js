const FORM_IDS = {
    login: "login-form-container",
    register: "register-form-container",
    confirm: "confirm-email-form-container",
};

function hideAllForms() {
    const loginForm = document.getElementById(FORM_IDS.login);
    const registerForm = document.getElementById(FORM_IDS.register);
    const confirmForm = document.getElementById(FORM_IDS.confirm);

    if (loginForm) { loginForm.style.display = "none"; }
    if (registerForm) { registerForm.style.display = "none"; }
    if (confirmForm) { confirmForm.style.display = "none"; }

    document.querySelectorAll(".register, .login").forEach(btn => {
        btn.style.borderBottom = "none";
    });
}

function showForm(state) {
    hideAllForms();

    if (state === "login") {
        const form = document.getElementById(FORM_IDS.login);
        if (form) { 
            form.style.display = "flex";
            
            const btn = form.querySelector(".login");
            if (btn) btn.style.borderBottom = "2px solid rgba(84, 60, 82, 1)";
        }
    }
    
    if (state === "register") {
        const form = document.getElementById(FORM_IDS.register);
        if (form) { 
            form.style.display = "flex";
            
            

            const btn = form.querySelector(".register")
            if (btn) btn.style.borderBottom = "2px solid rgba(84, 60, 82, 1)"
        }
    }
    
    if (state === "confirm") {
        const form = document.getElementById(FORM_IDS.confirm);
        if (form) { 
            form.style.display = "flex"; 
        }
    }
}

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".register").forEach(button => {
        button.onclick = () => showForm("register");
    });
    
    document.querySelectorAll(".login").forEach(button => {
        button.onclick = () => showForm("login");
    });
    showForm("register");
});