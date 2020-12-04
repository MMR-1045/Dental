
from django.contrib import admin
from django.urls import path,include

# appname='website'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),

]
