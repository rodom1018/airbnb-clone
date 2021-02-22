from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """ Review List Definition """

    list_display = ("__str__", "created", "count_messages")


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """ Review List Definition """

    list_display = ("__str__", "count_participants")
