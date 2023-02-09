from django.urls import path

from user_pass_mgt_2023.web2.views import UsersListView

urlpatterns = (
    path('', UsersListView.as_view(), name='index'),
)