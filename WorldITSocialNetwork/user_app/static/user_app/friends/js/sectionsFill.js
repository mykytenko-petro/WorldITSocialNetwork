import { PaginationProvider } from "/static/js/utils/paginationProvider.js"
import { friendsAllFriends, friendsRecomendations, friendsRequests } from "./DOM.js"

// dom
const friendsRequestsContainer = friendsRequests.querySelector(".cards")
const friendsRecomendationsContainer = friendsRecomendations.querySelector(".cards")
const friendsAllFriendsContainer = friendsAllFriends.querySelector(".cards")

// logic
const paginationUrl = document.querySelector('meta[name="paginationUrl"]').getAttribute('content')

new PaginationProvider(
    paginationUrl + "requests/",
    friendsRequestsContainer,
)

new PaginationProvider(
    paginationUrl + "recommendations/",
    friendsRecomendationsContainer,
)

new PaginationProvider(
    paginationUrl + "all_friends/",
    friendsAllFriendsContainer,
)