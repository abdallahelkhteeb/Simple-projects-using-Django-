from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('post_fun/<int:pk>', views.post_fun, name="post_fun")
]