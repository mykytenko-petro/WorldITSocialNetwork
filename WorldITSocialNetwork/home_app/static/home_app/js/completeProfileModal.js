const form = document.querySelector("#complete-profile form")
const button = document.querySelector("#complete-profile button")

button?.addEventListener(
    "click",
    () => {
        const formData = new FormData(form)
        
        fetch(form.action, {
            method : 'POST',
            headers: {
                'X-CSRFToken': CSRFToken,
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: formData
        })
        .then(async response =>{
            const data = await response.json()
            if (!response.ok){
                console.error(response.status)
                throw data
            }

            document.querySelector("#complete-profile").style.display = "none"
        })
        .catch(async (errors) => {
            alert(JSON.stringify(errors))
        })
    }
)