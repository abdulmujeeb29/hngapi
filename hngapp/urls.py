from django.urls import path 
from . import views 

urlpatterns =[
    path('api',views.create_person,name='create_person'),
    path('api/get',views.get_person,name='get_person'),
    path('api/<int:person_id>',views.get_person_by_id,name='get_person_by_id'),
    path('api/<str:person_name>',views.get_person_by_name,name="get_person_by_name"),
    
]