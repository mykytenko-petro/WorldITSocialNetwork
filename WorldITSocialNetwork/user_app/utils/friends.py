from ..models import User


def get_friend_requests(user):
    return User.objects.filter(
        sent_friendships__to_user = user,
        sent_friendships__status = 'pending'
    ).order_by('id')

def get_all_friends(user: User):
    sent_friend_ids = list(
        user.sent_friendships.filter(status = 'accepted').values_list('to_user_id', flat = True) # type: ignore
    )
    received_friend_ids = list(
        user.received_friendships.filter(status= 'accepted').values_list('from_user_id', flat= True) # type: ignore
    )
    friend_ids = sent_friend_ids + received_friend_ids
    return User.objects.filter(id__in= friend_ids).order_by('id')

def get_friend_recommendations(user: User):
    sent_busy_ids = list(user.sent_friendships.values_list('to_user_id', flat= True)) # type: ignore
    received_busy_ids = list(user.received_friendships.values_list('from_user_id', flat= True)) # type: ignore
    busy_ids = sent_busy_ids + received_busy_ids + [user.id] # type: ignore
    return User.objects.exclude(id__in = busy_ids).order_by('id')
    