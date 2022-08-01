from django.urls import path
from . import views
from django.urls import path,include             
urlpatterns = [
     
    path("register/", views.registeruser, name="registeruser"),
    path("login/", views.loginuser, name="loginuser"),
    path("logoutuser/", views.logoutuser, name="logoutuser"),
    path("room/<slug:pk>/", views.room, name="room"),
    path("usercon_card/<slug:pk>/", views.usercon_card, name="usercon_card"),
    path("usercon_card_update/<slug:pk>/", views.usercon_card_update, name="usercon_card_update"),
    path("pending_payment/<slug:pk>/", views.pending_payment, name="pending_payment"),
    path("profile/<slug:pk>/", views.profile, name="profile"),
    path('', include('homePage.urls')),
]
