
from email.mime import application
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.author.urls')),
    path('book/', include('applications.books.urls')),
]
