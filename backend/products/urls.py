from django.urls import path,include

from . import views

urlpatterns = [
    path('<int:pk>',views.ProductDetailView.as_view(),name = 'product_detail_view'),
    path('',views.ProductCreateAPIView.as_view(),name='product_create_view'),
    path('list/',views.ProductListCreateView.as_view(),name='product_list_create_view'),
    path('<int:pk>/update/',views.ProductUpdateView.as_view(),name = 'product_update_view'),
    path('<int:pk>/delete/',views.ProductDeleteView.as_view(),name = 'product_delete_view'),
    
]
