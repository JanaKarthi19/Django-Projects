from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.LoginPageResponse),
    path('login', views.LoginPageResponse, name='login'),
    path('logout', views.LogoutPageResponse, name='logout'),
    path('register', views.RegisterPageResponse),

    path('addinguser', views.RegisterUserResponse),
    path('accessing', views.UserLoginResponse, name='home'),

    path('home/id/<int:id>', views.HomePageResponse, name='Home_page'),
    path('add/id/<int:id>', views.AddListResponse, name='Add_todo'),
    path('update/id/<int:id>', views.AddingList, name='Update_todo'),


    path('edit/id/<int:id>/user_id/<int:user_id>', views.EdtPageResponse, name='edit_todo'),
    path("Update_Todo/id/<int:id>/user_id/<int:user_id>", views.EditedListResponse, name='edited_todo'),
    path("Delete_Todo/id/<int:id>/user_id/<int:user_id>", views.DeleteListResponse, name='delete_todo' ),
    path("Deleted_todo/id/<int:id>/user_id/<int:user_id>", views.DeletedListResponse, name='deleted_todo')
]
