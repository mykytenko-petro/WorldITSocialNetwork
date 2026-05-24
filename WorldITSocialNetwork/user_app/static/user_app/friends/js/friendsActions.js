const friendsActionsUrl = document.querySelector('meta[name="friendsActionsUrl"]').getAttribute('content')

export async function fetchFriendAction(mode, userId) {
    const url = friendsActionsUrl + `?mode=${mode}&user_id=${userId}`

    return await fetch(url, {
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
        return data
    })
    .catch(async (errors) => {
        alert(JSON.stringify(errors))
    })
}
    export async function handleDeleteClick(element, userId){
        const result = await fetchFriendAction(element.dataset.action, userId)
            if (result){
                const card = element.closest("[data-user-id]")
                if (card){
                    card.remove()
                }
            }
        }

export async function handleAcceptClick(element, userId){
    const result = await fetchFriendAction(element.dataset.action, userId)
    if (result){
        const card = element.closest('[data-user-id]')
        const friendList = document.querySelector('#friendsAllFriends.cards')
        if (card && friendList){
            const friendsCards = friendList.querySelector('button[data-action="delete"]')
            if (friendsCards){
                const deleteBtn = card.querySelector('button[data-action="delete"]')
                if (deleteBtn){
                    deleteBtn.remove()
                }
                element.textContent = 'Видалити друга'
                element.dataset = 'delete'
                
            }
        }
    }
        
}