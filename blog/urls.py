from django.urls import path, include

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.postsviews, name='home'),
    path('post/<int:post_id>/', views.postview ),
    path('profile/<int:user_id>', views.perfilview)
]
