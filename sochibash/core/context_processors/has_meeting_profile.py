from meeting.models import Profile


def has_profile(request):
    """Проверка, что у пользователя уже существует анкета для знакомства"""
    profile = Profile.objects.filter(author_id=request.user.id)
    if profile:
        return {
            'has_profile': True,
            'profile_id': profile[0].id
        }
    else:
        return {
            'has_profile': False
        }
