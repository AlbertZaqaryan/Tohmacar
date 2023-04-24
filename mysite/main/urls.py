from django.urls import path
from . import views


urlpatterns=[
   path('', views.index, name='index') ,
   path('parent/', views.parent, name='parent') ,
   path('child1/', views.child1, name='child1'),
   path('child2/', views.child2, name='child2'),
   path('child3/', views.child3, name='child3'),
   path('tree/', views.tree, name='tree') ,
]