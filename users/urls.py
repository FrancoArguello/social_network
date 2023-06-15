from django.urls import path
from .views import UserProfileView, EditProfile
app_name= "users"

urlpatterns = [
    path('<username>/', UserProfileView.as_view(), name="profile"),
    path('profile/editProfile', EditProfile, name = 'editProfile')
]
