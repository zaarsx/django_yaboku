from rest_framework import serializers

from slides import models


class SlideSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Slide
        fields = ('id', 'title', 'image', 'text')


