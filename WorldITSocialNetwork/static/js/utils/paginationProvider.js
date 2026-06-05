export class PaginationProvider {
    constructor(
        url, container,
        customThreshold,
        queryParams,
        rootMargin = "200px"
    ) {
        this.url = url
        this.currentPage = 1
        this.isLoading = false
        this.queryParams = queryParams

        this.scrollThreshold = customThreshold ?? document.createElement("hr")
        this.scrollThreshold.style.opacity = "0"
        container.appendChild(this.scrollThreshold)

        this.observer = new IntersectionObserver(async (entries) => await this.observerCallback(entries), {
            rootMargin: rootMargin
        })
        this.observer.observe(this.scrollThreshold)
    }

    async observerCallback(entries) {
        if (entries[0].isIntersecting && this.isLoading == false) {
            this.isLoading = true

            const url = this.url + `?page=${this.currentPage}` + (this.queryParams ? this.queryParams : '')

            await fetch(url, {
                method: 'GET',
            })
                .then(async response => {
                    if (response.status === 204) {
                        this.observer.unobserve(this.scrollThreshold)
                        this.isLoading = false
                        return
                    }
                    
                    const data = await response.json()
                    if (!response.ok) {
                        console.error(data)
                    }
                    return data
                })
                .then(data => {
                    if (!data) return

                    this.scrollThreshold.insertAdjacentHTML('beforebegin', data.html)

                    this.currentPage++
                    this.isLoading = false
                    this.observer.unobserve(this.scrollThreshold)
                    this.observer.observe(this.scrollThreshold)
                })
        }
    }
}