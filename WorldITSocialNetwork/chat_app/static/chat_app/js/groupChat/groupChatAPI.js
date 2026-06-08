document.addEventListener("api:getSortedContacts", (e) => {
    fetch("/chat/contact_filter/", {method: "GET"})
        .then(response => response.json())
        .then(response => {
            document.dispatchEvent(new CustomEvent("dom:pasteFilteredContacts", {
                detail: {
                    html: response.html
                }
            }))
        })
})