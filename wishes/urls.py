from django.urls import path

from wishes.views import WishViewSet, CharacterViewSet

urlpatterns = [
    path(r'wish/', WishViewSet.as_view()),
    path(r'character/', CharacterViewSet.as_view()),
]