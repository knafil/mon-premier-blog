from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/welcome/', views.post_welcome, name='post_welcome'),
    path('post/login/', views.login, name='login'),	
    path('drafts/', views.post_draft_list, name='post_draft_list'),	
]


