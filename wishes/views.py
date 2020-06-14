from rest_framework import generics

from wishes.models import Wish, Character
from wishes.serializers import WishSerializer, CharacterSerializer


class CharacterViewSet(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class WishViewSet(generics.ListCreateAPIView):
    queryset = Wish.objects.all()
    serializer_class = WishSerializer




