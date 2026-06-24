const contactProviderUrl = document.querySelector("meta[name='contactProviderUrl']").getAttribute("content")

export async function getContactData(page) {
    const url = contactProviderUrl + `?page=${page}`

    return await fetch(url, { method: "GET" })
        .then(async response => {
            if (response.status === 204) {
                return
            }
    
            const data = await response.json()
            if (!response.ok) {
                console.error(data)
                return
            }
    
            return data
        })
}