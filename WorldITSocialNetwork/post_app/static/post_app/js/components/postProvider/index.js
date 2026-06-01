import { PaginationProvider } from "/static/js/utils/paginationProvider.js"

// dom
const postProvider = document.getElementById("postProvider")

// logic
let mode = "recommendations"
if (window.location.pathname === "/post/") {
    mode = "own_posts"
}

const baseUrl = postProvider.dataset.url

new PaginationProvider(
    baseUrl,
    postProvider,
    null,
    `&mode=${mode}`
)