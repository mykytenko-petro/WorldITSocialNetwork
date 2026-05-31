import { fetchFriendAction } from "./friendsActions.js"

const acceptButton = document.getElementById("acceptUsersButton")
const dismissButton = document.getElementById("dismissUsersButton")
const url = "/user/friends/"
const queryString = window.location.search
const urlParams = new URLSearchParams(queryString);

const mode = urlParams.get("mode")
const secondMode = urlParams.get("secondMode").slice(0, -1)

acceptButton.addEventListener("click", (event) => {
    fetchFriendAction(mode)
    window.location.href = url
})

dismissButton.addEventListener("click", (event) => {
    fetchFriendAction(secondMode)
    window.location.href = url
})