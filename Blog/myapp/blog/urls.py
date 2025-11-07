from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<str:post_id>", views.detail, name="detail"),
    path("New_url", views.new_url_view, name="new_url_page"),
    path("old_url", views.old_url_redirect, name="old_url"),
]