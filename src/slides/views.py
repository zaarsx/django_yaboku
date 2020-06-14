from rest_framework import generics

from slides.models import Slide
from slides.serializers import SlideSerializer


class SlideViewSet(generics.ListAPIView):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer