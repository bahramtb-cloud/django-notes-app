from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    

    path("login/", views.login_user),

    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(
            template_name="accounts/password_change.html"
        ),
        name="password_change",
        ),

    path(
        "password-change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="accounts/password_change_done.html"
        ),
        name="password_change_done",
        ),

    path("register/", views.register, name="register"),
]

