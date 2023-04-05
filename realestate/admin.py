from django.contrib import admin
from .models import *


class UsersAdmin(admin.ModelAdmin):
    list_display=('user','password')


class SivangangaiAdmin(admin.ModelAdmin):
    list_display=('owner','date','type','image','address','size','are')


class ThanjavurAdmin(admin.ModelAdmin):
    list_display=('owner','date','type','image','address','size','are')


class ThiruvallurAdmin(admin.ModelAdmin):
    list_display=('owner','date','type','image','address','size','are')


class CommentsAdmin(admin.ModelAdmin):
    list_display=('name','number','email','comment')



class ContactsAdmin(admin.ModelAdmin):
    list_display=('name','number','email','message')

admin.site.register(Users,UsersAdmin)
admin.site.register(Sivangangai,SivangangaiAdmin)
admin.site.register(Thiruvallur,ThiruvallurAdmin)
admin.site.register(Thanjavur,ThanjavurAdmin)
admin.site.register(Comments,CommentsAdmin)
admin.site.register(Contacts,ContactsAdmin)
# Register your models here.
