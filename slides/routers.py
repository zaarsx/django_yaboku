from rest_framework import routers

from slides.views import SlideViewSet

router = routers.DefaultRouter()

router.register(r'slide', SlideViewSet)