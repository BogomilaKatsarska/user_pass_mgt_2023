from django.urls import path

from user_pass_mgt_2023.web.views import SignUpView

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign up'),
)