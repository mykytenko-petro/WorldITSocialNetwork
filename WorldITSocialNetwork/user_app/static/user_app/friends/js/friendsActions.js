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
    // const result = await fetchFriendAction(element.dataset.action, userId)
    // if (result){
    //     const card = element.closest("[data-user-id]")
    //     card.remove()
    // }
    // await fetchFriendAction(element.dataset.action, result)
    // return data
}

