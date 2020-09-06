""" Users urls."""

#Django
from django.urls import path

#Views
from users import views

urlpatterns = [

    # Managment
    path(
      route = 'login',
      view = views.login_view,
      name='login'
    ),

    path(
      route = 'logout',
      view = views.logout_view,
      name='logout'
    ),

    path(
      route = 'sign_up',
      view = views.SignUpView.as_view(),
      name='sign_up'
    ),

    path(
      route = 'me/profile',
      view = views.update_profile,
      name='update_profile'
    ),

    # Posts
    path(
      route = '<str:username>/',
        view= views.UserDetailView.as_view(),
      name = 'detail'
    ),
]