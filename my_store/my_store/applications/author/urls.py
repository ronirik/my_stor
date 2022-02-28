from django.urls import path
from .views import AuthorListView

urlpatterns = [
    path('auth-list/', AuthorListView.as_view())
]