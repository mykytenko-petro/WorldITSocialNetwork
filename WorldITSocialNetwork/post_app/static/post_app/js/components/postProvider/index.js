import { PaginationProvider } from "/static/js/utils/paginationProvider.js"

// dom
const postProvider = document.getElementById("postProvider")

// logic
let mode = "own_posts"
const baseUrl = postProvider.dataset.url
const userId = postProvider.dataset.userId
const url = `/user/${userId}?userId=${userId}/`

new PaginationProvider(
    baseUrl,
    postProvider,
    null,
    `&mode=${mode}&user_id=${userId}`
)