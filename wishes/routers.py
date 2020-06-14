from rest_framework import routers

from wishes.views import WishViewSet, CharacterViewSet

router = routers.DefaultRouter()

router.register(r'wish', WishViewSet)
router.register(r'character', CharacterViewSet)