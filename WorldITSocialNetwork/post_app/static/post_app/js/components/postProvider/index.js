import { PaginationProvider } from "/static/js/utils/paginationProvider.js"

const postProvider = document.getElementById("postProvider")
const baseUrl = postProvider.dataset.url
const userId = postProvider.dataset.userId

let queryParams
if (userId) {
    queryParams = `&mode=own_posts&user_id=${userId}`
} else {
    queryParams = `&mode=recommendations`
}

new PaginationProvider(
    baseUrl,
    postProvider,
    null,
    queryParams
)