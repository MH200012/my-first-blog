from django.urls import path
from blog import views
from django.contrib import admin
from .forms import PostForm

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('admin/', admin.site.urls),

]


