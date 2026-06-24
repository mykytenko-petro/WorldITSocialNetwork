import { fetchFriendAction } from "./friendsActions.js"

const acceptButton = document.getElementById("acceptUsersButton")
const dismissButton = document.getElementById("dismissUsersButton")
const url = "/user/friends/"
const queryString = window.location.search
const urlParams = new URLSearchParams(queryString);

const mode = urlParams.get("mode")
const secondMode = urlParams.get("secondMode").slice(0, -1)

acceptButton.addEventListener("click", async (event) => {
    event.preventDefault(); // Prevents form submission reloads if applicable
    
    const success = await fetchFriendAction(mode);
    if (success) {
        window.location.href = url;
    } else {
        alert("Something went wrong with the accept action.");
    }
})

dismissButton.addEventListener("click", async (event) => {
    event.preventDefault();
    
    const success = await fetchFriendAction(secondMode);
    if (success) {
        window.location.href = url;
    } else {
        alert("Something went wrong with the dismiss action.");
    }
})