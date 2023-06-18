from django import views
from django.urls import path
from .views import UserProfileView, EditProfile, NewFollower, RemoveFollower, ListFollowers
app_name= "users"

urlpatterns = [
    path('<username>/', UserProfileView.as_view(), name="profile"),
    path('profile/editProfile', EditProfile, name = 'editProfile'),
    
    path('profile/<int:pk>/followers/add', NewFollower.as_view(), name='add-follower'),
	path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    path('users/profile/<int:pk>/followers/', ListFollowers.as_view(), name='followers-list'),
    
]
