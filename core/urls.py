from django.urls import path
from . import views  # ou outro app que tenha a view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('escolha',views.escolha, name='escolha'),
    path('cadastro/cliente/', views.cadastro_cliente, name='cadastro_cliente'),
    path('cadastro/comercio/', views.cadastro_comercio, name='cadastro_comercio'),
    path('login/cliente',views.login_cliente, name='login_cliente'),
    path('login/comercio',views.login_comercio, name='login_comercio'),
    path('home/cliente',views.home_cliente, name='home_cliente'),
    path('home/comercio',views.home_comercio, name='home_comercio'),
    path('perfil/comercio',views.perfil_comercio, name='perfil_comercio'),
    path('estoque',views.estoque, name='estoque'),
    path('estoque/adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('estoque/editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('estoque/remover/<int:produto_id>/', views.remover_produto, name='remover_produto'),
    path('perfil/cliente',views.perfil_cliente, name='perfil_cliente'),
    path('comentarios/cliente',views.comentario_cliente, name='comentario_cliente'),
    path('estabelecimento/favoritados',views.estabelecimento_favoritados, name='estabelecimento_favoritados'),
    path('buscar', views.buscar_comercios, name='buscar_comercios'),
    path('comercio/<int:comercio_id>/', views.perfil_comercio_publico, name='perfil_comercio_publico'),
    path('comercio/<int:comercio_id>/catalogo/', views.ver_catalogo, name='ver_catalogo'),
    path('comercio/<int:comercio_id>/favoritar/', views.favoritar_comercio, name='favoritar_comercio'),
    path('comercio/codigo/compra',views.comercio_codigo_compra, name='comercio_codigo_compra'),
    path('feedback/produtos',views.feedback_produtos, name='feedback_produtos'),
    path('carrinho/',views.carrinho, name='carrinho'),
    path('adicionar-ao-carrinho/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('finalizar-compra/', views.finalizar_compra, name='finalizar_compra'),
    path('cancelar-pedido/', views.cancelar_pedido, name='cancelar_pedido'),
    path('finalizar-compra/', views.finalizar_compra, name='finalizar_compra'),
    path('compra/<str:codigo>/compra', views.comercio_codigo_compra, name='comercio_codigo_compra'),
    path('compra/<str:codigo>/entregue/', views.marcar_entregue, name='marcar_entregue')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#path('',views., name=''),
