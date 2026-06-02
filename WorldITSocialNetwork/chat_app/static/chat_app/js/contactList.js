import { PaginationProvider } from "/static/js/utils/paginationProvider.js"

const container = document.querySelector(".contact-container")
const url = container.dataset.url

new PaginationProvider(
    url,
    container,
    null,
    "200px",
    container,
)