from django.contrib import admin
from .models import ProfileData, About, SocialLink, Tool, Service, Project, Category, Post, PostCategory, Tag


admin.site.register(ProfileData)
admin.site.register(About)

admin.site.register(SocialLink)
admin.site.register(Tool)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Tag)