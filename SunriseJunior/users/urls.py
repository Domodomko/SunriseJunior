from django.urls import path
from .views import *


urlpatterns = [
    # API
    path('api/signup', UserCreateView.as_view(), name='api_user_sign_up'),
    path('api/signin', UserSignInView.as_view(), name='api_sign_in'),
    path('api/user', UserUpdateView.as_view(), name='api_user_update'),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    # Templates
    path('user', user_detail_view, name='user'),
    path('user_update', user_update_view, name='user_update'),
    path('signin', sign_in_view, name='sign_in'),
    path('signout', sign_out_view, name='sign_out'),
    path('signup', sign_up_view, name='sign_up'),
]