import { mainButton, requestsButton, recomendationsButton, allFriendsButton } from "./DOM.js";
import { showBox } from "./displayLogic.js"

// tabs
mainButton.addEventListener("click", () => {
    showBox("friendsMain")
})

requestsButton.forEach((element) => {
    element.addEventListener("click", () => {
        showBox("friendsRequests")
    })
})

recomendationsButton.forEach((element) => {
    element.addEventListener("click", () => {
        showBox("friendsRecomendations")
    })
})

allFriendsButton.forEach((element) => {
    element.addEventListener("click", () => {
        showBox("friendsAllFriends")
    })
})

// actions
document.addEventListener("click", async (event) => {
    const element = event.target

    console.log(element)

    if (!element.matches("[data-action]")) {
        return
    }
    
    console.log(element.dataset.action)
})