from django.contrib.auth.views import LoginView
from django.urls import path

from user_pass_mgt_2023.web.views import SignUpView, sign_in, SignOutView

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    # path('sign-in/', sign_in, name='sign in'),
    path('sign-in/', LoginView.as_view(), name='sign in'),
    path('sign-out/', SignOutView.as_view(), name='sign out'),
)