from rest_framework import serializers

from wishes import models


class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Character
        fields = ('id', 'name', 'image')


class WishSerializer(serializers.ModelSerializer):

    author = CharacterSerializer(read_only=True)

    id = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(read_only=True)
    published = serializers.BooleanField(read_only=True)

    class Meta:
        model = models.Wish
        fields = ('id', 'author', 'text', 'created', 'published')

    def create(self, validated_data):
        wish = models.Wish(**validated_data)
        wish.author = models.Character.objects.order_by('?').first()
        wish.save()
        return wish

