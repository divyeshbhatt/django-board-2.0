from django.contrib import admin
from . models import Board, Topic, Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ['topics', 'created_by']

class TopicAdmin(admin.ModelAdmin):
	list_display = ['subject', 'board']

class BoardAdmin(admin.ModelAdmin):
	list_display = ['name', 'description']


admin.site.register(Board, BoardAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
