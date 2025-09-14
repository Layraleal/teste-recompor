from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView


urlpatterns = [ 
    path("login/", views.login, name = "logar"),
    path("register", views.register, name="register"), 
    path('deslogar/',views.deslogar,name='deslogar'),
     path("reset-password/", CustomPasswordResetView.as_view(), name="password_reset"),
    path("reset-password/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("reset-password/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
] 