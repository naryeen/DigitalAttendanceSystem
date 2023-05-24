from django.urls import path,include
from .views import *

# app_name = 'core'


urlpatterns = [
    path('', home, name= 'home'),
    path('index/', aindex, name= 'index'),
    path('bindex/', it_b_index, name= 'bindex'),

    path('ajax/', ajax, name= 'ajax'),
    path('scan/',scan,name='scan'),
    path('profiles/', profiles, name= 'profiles'),
    path('bprofiles/', bprofiles, name= 'bprofiles'),

    path('details/', details, name= 'details'),
    path('add_profile/',add_profile,name='add_profile'),
    path('edit_profile/<int:id>/',edit_profile,name='edit_profile'),
    path('delete_profile/<int:id>/',delete_profile,name='delete_profile'),
    path('clear_history/',clear_history,name='clear_history'),
    path('reset/',reset,name='reset'),
    path('download/',download,name='download'),


]
