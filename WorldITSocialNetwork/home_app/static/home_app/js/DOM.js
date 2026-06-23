fetch("/user/friends-pagination/home?page=1", {
    method: "GET"
})
.then(response => {
    if (!response.ok) {
        console.error(response.status)
        return
    }

    return response
})
.then(response => response.json())
.then(data => {
    const container = document.querySelector(".requests .container")

    container.innerHTML = data.html
})