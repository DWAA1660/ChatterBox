from django.contrib import admin
from chatterbox.ext.django_chatterbox.model_admin import StatementAdmin, TagAdmin
from chatterbox.ext.django_chatterbox.models import Statement, Tag


admin.site.register(Statement, StatementAdmin)
admin.site.register(Tag, TagAdmin)
