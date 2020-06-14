from django.urls import path

from slides.views import SlideViewSet

urlpatterns = [
    path(r'slide/', SlideViewSet.as_view()),
]