

from django.contrib import admin
from django.urls import path, include
from blog.views import post_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/", post_list),
    path('blog/', include('blog.urls'))
]
