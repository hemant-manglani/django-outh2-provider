from django.urls import path, include
from users import views
import oauth2_provider.views as oauth2_views

urlpatterns = [
    # path('', views.index, name='index'),
    path(r'users/login/',views.Login.as_view()),
    path(r'users/check/',views.Check.as_view()),
    path(r'users/register/', views.UserRegister.as_view(), name='register'),
    # path('logout', views.user_logout, name='logout'),
    # path('users/', views.userList.as_view(), name='user_list'),
    # path('refresh_token', views.TokenRefresh.as_view(), name='logout'),

]
