// dom
const postProvider = document.getElementById("postProvider")
const scrollThreshold = postProvider.querySelector("hr")

// logic
let mode
if (window.location.pathname === "/") {
    mode = "recommendations"
} else if (window.location.pathname === "/post/") {
    mode = "own_posts"
}

let currentPage = 0
let isLoading = false

const observer = new IntersectionObserver(async (entries) => {
    if (entries[0].isIntersecting && isLoading == false){
        isLoading = true
        currentPage++

        console.log(mode)

        const formData = new FormData();
        formData.append('mode', mode);
        formData.append('page', currentPage);

        fetch(postProvider.dataset.url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': CSRFToken,
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: formData
        })
        .then(async response =>{
            if (response.status === 204) {
                return
            }

            const data = await response.json()
            if (!response.ok){
                throw data
            }
            
            scrollThreshold.insertAdjacentHTML('beforebegin', data.html)
        })
        .catch(async (errors) => {
            alert(JSON.stringify(errors))
        })

        isLoading = false
    }
}, {rootMargin: '200px'})

observer.observe(scrollThreshold)
