const buttonCreatePost = document.getElementById("button-create-post")
const postMenu = document.getElementById("create-post-menu")

postMenu.style.display = "none"
buttonCreatePost.addEventListener("click", () => {
    postMenu.style.display = "flex"
})