from django.contrib import admin
from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),  # This line includes the admin site URLs

]


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('admin/', admin.site.urls),  # This line includes the admin site URLs
]