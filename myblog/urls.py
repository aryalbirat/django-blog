from django.contrib import admin
from django.urls import path, include
from blog.views import default_route

# Everything starting with this goes to the specific file or directory
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", default_route ),
    path("blog/", include("blog.urls")),
    # everything starting with /blog/ goes into blog/urls.p
]
