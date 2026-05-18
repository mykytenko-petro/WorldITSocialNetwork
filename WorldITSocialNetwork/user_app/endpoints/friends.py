from django.views.generic.base import View
from django.http import HttpRequest, JsonResponse
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404

from ..utils import get_all_friends, get_friend_recommendations, get_friend_requests
from ..models import User, Friendship


class FriendCardView(View):
    def post(self, request: HttpRequest):
        mode = request.POST.get("mode")
        user_count = request.POST.get("page")

        # return self.get_users(mode, int(user_count))  # type: ignore

    @staticmethod
    def get_user_cards(user: User, mode: str, page_count: int):
        # TODO: create and use user query utils instead of hardcoded all users
        # queryset = User.objects.all()

        match mode:
            case "requests":
                queryset = get_friend_requests(user)

            case "recommendations":
                queryset = get_friend_recommendations(user)

            case "all_friends":
                queryset = get_all_friends(user)

            case _:
                return

        if mode == "requests":
            paginator = Paginator(queryset, 3)
        else:
            paginator = Paginator(queryset, 6)

        users = paginator.get_page(page_count)

        if page_count > paginator.num_pages:
            return

        return render_to_string(
            template_name="user_app/friends/particles/user_card.html",
            context={"users": users, "mode": mode},
        )


class AddFriendsView(View):
    def post(self, request):
        user_id = request.POST.get("user_id")

        if not user_id:
            return JsonResponse({"eror": "ID користувача не надано"}, status=400)
        
        to_user = get_object_or_404(User, id=user_id)
        from_user = request.user

        if from_user == to_user:
            return JsonResponse(
                {"error": "Ви не можете додати себе в друзі"}, status=400
            )
        
        friend_already_1 = Friendship.objects.filter(
            to_user=user_id, from_user=from_user, status = 'accepted'
        ).exists()
        friend_already_2 = Friendship.objects.filter(
            to_user=to_user, from_user = user_id, status = 'accepted'
        ).exists()

        if friend_already_1 or friend_already_2:
            return JsonResponse(
                {'message': 'Цей користувач вже є у вас в друзях'},
                status = 400
            )

        friendship, created = Friendship.objects.get_or_create(
            from_user=from_user, to_user=to_user, defaults={"status": "pending"}
        )
        
        if not created:
            return JsonResponse(
                {"message": "Запит вже було надіслано раніше"}, status=400
            )

        return JsonResponse({"message": "Запит на дружбу успішно створено"})
