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

    if (!element.matches("[data-action]")) {
        return
    }

    const userId = element.closest("[data-user-id]").dataset.userId
    const result = await fetchFriendAction(element.dataset.action, userId)
    if (result){
        const card = element.closest("[data-user-id]")
        card.remove()
    }
    await fetchFriendAction(element.dataset.action, userId)
})