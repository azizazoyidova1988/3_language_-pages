from django.contrib import admin
from .models import Subscribers, Post, Follower,Advertising

admin.site.register(Subscribers)
admin.site.register(Post)
admin.site.register(Follower)
admin.site.register(Advertising)