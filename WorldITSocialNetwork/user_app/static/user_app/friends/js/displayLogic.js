import { friendsMain, friendsRequests, friendsRecomendations, friendsAllFriends, sideButtons } from "./DOM.js"


export function showBox(boxName) {
    if(boxName === "friendsMain"){
        friendsMain.style.display = "flex"
        friendsRequests.style.display = "none"
        friendsRecomendations.style.display = "none"
        friendsAllFriends.style.display = "none"


        sideButtons[0].classList.add('selected')
        sideButtons[1].classList.remove('selected')
        sideButtons[2].classList.remove('selected')
        sideButtons[3].classList.remove('selected')

    }

    if(boxName === "friendsRequests"){
        friendsMain.style.display = "none"
        friendsRequests.style.display = "flex"
        friendsRecomendations.style.display = "none"
        friendsAllFriends.style.display = "none"

        sideButtons[0].classList.remove('selected')
        sideButtons[2].classList.remove('selected')
        sideButtons[3].classList.remove('selected')
        sideButtons[1].classList.add('selected')
    }

    if(boxName === "friendsRecomendations"){
        friendsMain.style.display = "none"
        friendsRequests.style.display = "none"
        friendsRecomendations.style.display = "flex"
        friendsAllFriends.style.display = "none"

        sideButtons[0].classList.remove('selected')
        sideButtons[1].classList.remove('selected')
        sideButtons[3].classList.remove('selected')
        sideButtons[2].classList.add('selected')
    }

    if(boxName === "friendsAllFriends"){
        friendsMain.style.display = "none"
        friendsRequests.style.display = "none"
        friendsRecomendations.style.display = "none"
        friendsAllFriends.style.display = "flex"

        sideButtons[0].classList.remove('selected')
        sideButtons[1].classList.remove('selected')
        sideButtons[2].classList.remove('selected')
        sideButtons[3].classList.add('selected')
    }
}

showBox("friendsMain")