from django.contrib import admin
from django.urls import path, include

from django.http import HttpResponse

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("todo.urls")),  #n i.e. if the URL path is empty, it will be handled in "todo" folder 

    # path("", home, name="home"),
]