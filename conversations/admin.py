from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Message)
class ListAdmin(admin.ModelAdmin):

    """ Review List Definition """

    pass


@admin.register(models.Conversation)
class ListAdmin(admin.ModelAdmin):

    """ Review List Definition """

    pass
