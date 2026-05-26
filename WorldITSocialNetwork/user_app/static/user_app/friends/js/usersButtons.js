// import {deleteCard} from "./friendsActions.js"
import { fetchFriendAction } from "./friendsActions.js"

const acceptButton = document.getElementById("acceptUsersButton")
const dismissButton = document.getElementById("dismissUsersButton")
const url = "/user/friends/"
const queryString = window.location.search
const urlParams = new URLSearchParams(queryString);

const mode = urlParams.get("mode").slice(0, -1)
const userId = urlParams.get("userId")
console.log(userId)

console.log(mode)

acceptButton.addEventListener("click", (event) => {
    window.location.href = url
})

dismissButton.addEventListener("click", (event) => {
    // deleteCard()
    window.location.href = url
    fetchFriendAction(mode,)

})