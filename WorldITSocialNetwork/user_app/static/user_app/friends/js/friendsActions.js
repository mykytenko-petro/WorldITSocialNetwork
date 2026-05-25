const friendsActionsUrl = document.querySelector('meta[name="friendsActionsUrl"]').getAttribute('content')

export async function fetchFriendAction(mode, userId, element) {
    const url = friendsActionsUrl + `?mode=${mode}&user_id=${userId}`

    await fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': CSRFToken,
        },
    })
        .then(async response => {
            const data = await response.json()
            if (!response.ok) {
                throw data
            }

            deleteCard(userId, element)

            if (mode === "accept") {
                addCardToAllFriends(data.html)
            }
        })
        
}

function deleteCard(id, element) {
    const card = element.closest("[data-user-id]")
    card.remove()
}

function addCardToAllFriends(html) {
    const allFriendsDiv = document.querySelector("#friends-list")

    allFriendsDiv.innerHTML += html
}