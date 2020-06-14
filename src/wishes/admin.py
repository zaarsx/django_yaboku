from django.contrib import admin

from wishes.models import Wish, Character


@admin.register(Character)
class CharacterModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Wish)
class WishModelAdmin(admin.ModelAdmin):
    pass
