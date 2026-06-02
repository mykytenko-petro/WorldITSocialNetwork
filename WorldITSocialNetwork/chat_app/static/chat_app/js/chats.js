const membersStep = document.querySelector('[data-step="members"]')
const detailsStep = document.querySelector('[data-step="details"]')
const nextButton = document.querySelector(".new-group-next")
const backButton = document.querySelector(".new-group-back")

const showStep = (stepName) => {
    membersStep.classList.toggle("is-active", stepName === "members")
    detailsStep.classList.toggle("is-active", stepName === "details")
}

nextButton.addEventListener("click", () => showStep("details"))
backButton.addEventListener("click", () => showStep("members"))
