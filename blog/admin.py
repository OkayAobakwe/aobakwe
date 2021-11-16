from django.contrib import admin
from .models import Entry, Comment
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'body', 'created_on', 'active')
	list_filter = ('active', 'created_on')
	search_fields = ('name', 'email', 'body')
	actions = ['approved_comments']

	def approved_comments(self, request, queryset):
		queryset.update(active=True)

admin.site.register(Entry)
admin.site.register(Comment)