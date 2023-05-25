from django.contrib import admin
from django.urls import path
from recipe import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.last_views, name='main'),
    path('all/', views.all_categories, name='category_list'),
]