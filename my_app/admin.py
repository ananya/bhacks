from django.contrib import admin
from my_app.models import Post,Comment,User_info,Pairing

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User_info)
admin.site.register(Pairing)