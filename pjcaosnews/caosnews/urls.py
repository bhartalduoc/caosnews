from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('categorias',views.index,name='categorias'),
    path('periodistas',views.index,name='periodistas'),
    path('contacto',views.index,name='contacto'),
    path('noticia1',views.index,name='noticia1')

]