const dialog = document.querySelector("#complete-profile")
const button = dialog.querySelector("button")

dialog?.showModal()

button?.addEventListener(
    "click",
    () => {
        const form = dialog.querySelector("form")
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

            dialog.close()
        })
        .catch(async (errors) => {
            alert(JSON.stringify(errors))
        })
    }
)