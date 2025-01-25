from django.urls import path
from . import views
app_name = 'vegproduct'
urlpatterns = [
    path('', views.vegetable_list, name='vegetable_list'), 
      # List and search vegetables

]
