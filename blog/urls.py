from django.urls import path
from .views import PostIndex, PostShow

urlpatterns = [
    path('', PostIndex.as_view()),
    path('<int:pk>/', PostShow.as_view()),
]
