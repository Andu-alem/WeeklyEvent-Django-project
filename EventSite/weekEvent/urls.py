from django.contrib import admin
from django.urls import path, re_path
from . import views

app_name = "weekEvent"
urlpatterns = [
    path(r'uploadImage/', views.DataUpload.as_view(), name="post_event"),
    path(r'<int:pk>/', views.EventDetailView.as_view(), name="event_detail"),
    path(r'create_user/', views.UserRegisterationView.as_view(), name="register"),
    path(r'login/', views.Login.as_view(), name="login"),
    path(r'logout/', views.Logout.as_view(), name="logout"),
    re_path(r'(?P<date>[a-zA-Z]{0,})/?', views.Index.as_view(), name="index"),
]