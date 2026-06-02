import { mainButton, requestsButton, recomendationsButton, allFriendsButton } from "./DOM.js"
import { showBox } from "./displayLogic.js"
import { fetchFriendAction } from "./friendsActions.js"

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
    const parent = element.closest("[data-user-id]")
    const buttons = parent.querySelectorAll("button")
    const mode = buttons[0].dataset.action
    const secondMode = buttons[1].dataset.action
    const userId = element.closest("[data-user-id]").dataset.userId
    const url = `/user/${userId}?mode=${mode}&secondMode=${secondMode}/`
    console.log(userId)
    window.location.href = url
    // await fetchFriendAction(element.dataset.action, userId, element)
})