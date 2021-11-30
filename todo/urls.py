from django.urls import path
from .import views



urlpatterns = [
    path('',views.home,name="home"),
    path('delete/<pk>', views.delete, name='delete'),
    path('cross/<pk>', views.cross, name='cross'),
    path('uncross/<pk>', views.uncross, name='uncross'),
    path('edit/<pk>', views.edit, name='edit'),
    
   
]