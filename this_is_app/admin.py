from django.contrib import admin
from this_is_app.models import Post, CategoryPost, Commentary, Likes, PredlojennieNovosti
# Register your models here.
admin.site.register(CategoryPost)
admin.site.register(Post)
admin.site.register(Commentary)
admin.site.register(Likes)
admin.site.register(PredlojennieNovosti)