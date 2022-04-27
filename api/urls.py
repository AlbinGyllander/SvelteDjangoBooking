from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_view, name='api-login'),
    path('logout/', views.logout_view, name='api-logout'),
    path('session/', views.session_view, name='api-session'),
    path('getUserDataGeneral/', views.getUserDataGeneral, name='api-getUserDataGeneral'),
    path('isAuthenticated/', views.isAuthenticad, name='api-isAuth'),
    path('registerUser/', views.registration_view, name='api-registration'),

    
]