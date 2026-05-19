import { mainButton, requestsButton, recomendationsButton, allFriendsButton } from "./DOM.js";
import { showBox } from "./displayLogic.js"

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