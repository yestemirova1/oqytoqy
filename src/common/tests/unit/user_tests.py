from django.contrib.auth.models import User

from common.models import Profile


def test_user(db) -> None:
    user = User.objects.create_user(
        username='username', password='password',
    )
    profiles = Profile.objects.all()
    assert profiles.count() == profiles.filter(user=user).count() == 1
