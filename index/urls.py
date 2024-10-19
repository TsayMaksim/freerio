from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('category/<int:pk>', views.news_category_page),
    path('news/<int:pk>', views.news_page)
]