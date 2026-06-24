const friendsActionsUrl = document.querySelector('meta[name="friendsActionsUrl"]').getAttribute('content')

export async function fetchFriendAction(mode) {
    const url = friendsActionsUrl + `&mode=${mode}`

    return await fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': CSRFToken,
        },
    })
        .then(response => {
            return response.ok
        })
}