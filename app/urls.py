from django.urls import path, include
from . import views

urlpatterns = [
    path('agregarCliente',views.agregar_cliente),
    path('',views.index),
    path('addCliente', views.Cliente_Create.as_view(), name="cliente_crear"),
    path('listar_clientes',views.listar_clientes),
    path('editar_cliente/<int:cliente_id>', views.editar_cliente),
    path('borrar_cliente/<int:cliente_id>', views.borrar_cliente),
    path('index',views.index),
    path('locales',views.locales),
    path('quienes_somos',views.quienes_somos),
]