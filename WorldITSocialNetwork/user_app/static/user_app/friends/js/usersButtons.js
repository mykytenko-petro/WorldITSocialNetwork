// import {deleteCard} from "./friendsActions.js"

const acceptButton = document.getElementById("acceptUsersButton")
const dismissButton = document.getElementById("dismissUsersButton")
const url = "/user/friends/"
const queryString = window.location.search
const urlParams = new URLSearchParams(queryString);

const mode = urlParams.get("mode").slice(0, -1)

console.log(mode)

acceptButton.addEventListener("click", (event) => {
    window.location.href = url
})

dismissButton.addEventListener("click", (event) => {
    // deleteCard()
    window.location.href = url

    fetch(`friends-actions/`, )
})