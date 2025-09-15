from django.contrib import admin
from django.urls import path, include
from blog.views import post_list

# Everything starting with this goes to the specific file or directory
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", post_list),
    path("blog/", include("blog.urls")),
    # everything starting with /blog/ goes into blog/urls.p
]
