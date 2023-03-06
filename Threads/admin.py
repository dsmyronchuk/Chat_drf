from Threads.models import *
from django.contrib import admin


class ThreadAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_participants', 'created', 'updated', )
    list_display_link = ('id', 'get_participants', 'created', 'updated', )
    search_fields = ('id', 'get_participants', 'created', 'updated', )

    def get_participants(self, obj):
        return ", ".join([p.username for p in obj.participants.all()])

    get_participants.short_description = 'Participants'
    get_participants.admin_order_field = 'participants__username'


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'text', 'thread', 'created', 'is_read', )
    list_display_link = ('id', 'sender', 'text', 'thread', 'created', 'is_read', )
    search_fields = ('id', 'sender', 'text', 'thread', 'created', 'is_read', )


admin.site.register(Thread, ThreadAdmin)
admin.site.register(Message, MessageAdmin)
