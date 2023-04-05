from django.urls import path
from . import views
urlpatterns=[
    path('',views.frontpage,name='front'),
    path('login',views.login,name='login'),
    path('check',views.check,name='check'),
    path('selection',views.selection,name='selection'),
    path('register',views.register,name='register'),
    path('viewproperty',views.viewproperty,name='viewproperty'),
    path('about',views.about,name='about'),
    path('posts',views.posts,name='posts'),
    path('comment',views.comment,name='comment'),
    path('openshed',views.open,name='open'),
    path('closedshed',views.closed,name='closed'),
    path('contact',views.contact,name='contact'),
    path('coldshed',views.cold,name='cold')
]