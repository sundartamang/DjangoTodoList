from django.urls import path
from .views import (
    home,
    delete,
    update,
    cross,
    uncross
)

app_name = 'core'
urlpatterns = [
    path('', home.as_view(), name='home'),
    path('delete/<str:pk>/', delete, name='delete'),
    path('update/<str:pk>/', update, name='update'),
    path('cross/<str:pk>/', cross, name='cross'),
    path('uncross/<str:pk>/', uncross, name='uncross'),
]