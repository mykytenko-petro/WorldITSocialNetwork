from ..models import User, Friendship


def get_friend_requests(user):
    return User.objects.filter(
        sent_friendships__to_user=user,
        sent_friendships__status="pending"
    ).order_by("id")


def get_all_friends(user: User):
    sent_friend_ids = list(
        user.sent_friendships.filter(status="accepted").values_list("to_user_id", flat=True)  # type: ignore
    )
    received_friend_ids = list(
        user.received_friendships.filter(status="accepted").values_list("from_user_id", flat=True)  # type: ignore
    )
    friend_ids = sent_friend_ids + received_friend_ids

    return User.objects.filter(id__in=friend_ids).order_by("id")


def get_friend_recommendations(user: User):
    sent_busy_ids = list(user.sent_friendships.values_list("to_user_id", flat=True))  # type: ignore
    received_busy_ids = list(user.received_friendships.values_list("from_user_id", flat=True))  # type: ignore
    busy_ids = sent_busy_ids + received_busy_ids + [user.id]  # type: ignore

    return User.objects.exclude(id__in=busy_ids).order_by("id")

def add_friend_request(user, other_user):
    
    Friendship.objects.get_or_create(from_user= user, to_user = other_user, defaults={'status': 'pending'})
    return {'label': 'Очікування'}

# видаляємо користувача із рекомендації
def dismiss_recommendation(user, other_user):
    
    Friendship.objects.get_or_create(from_user= user, to_user = other_user, defaults={'status': 'dismissed'})
    return {'remove': True}
# додаємо у друзі
def accept_friend_request(user, other_user):
    friendship = Friendship.objects.filter(from_user = other_user, to_user = user).first()
    friendship.status = 'accepted'
    friendship.save()
    
    return {'remove': True, 'friend': other_user}
# видаляємо запит або дружбу
def delete_friendship(user, other_user):
    friendship = Friendship.objects.filter(from_user = user, to_user = other_user).first()
    if not friendship:
        friendship = Friendship.objects.filter(from_user = other_user, to_user = user).first()
    if friendship:
        friendship.delete()
    return {'remove': True}