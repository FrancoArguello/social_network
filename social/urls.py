from django.urls import path
from .views import PostDelete, PostEdit
app_name = 'social'


urlpatterns = [
    path('post/delete/<int:pk>', PostDelete.as_view(), name="post-delete"),
    path('post/edit/<int:pk>/', PostEdit.as_view(), name='post-edit'),
]
