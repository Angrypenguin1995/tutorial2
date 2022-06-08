from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.decorators import api_view

from .models import Product
from .serializers import ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    lookup_field = 'pk'
    
    
class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
     

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
    
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        
        if content is None:
            content =  title
        
        serializer.save(content = content)
        

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        
        if content is None:
            content = title
        
        serializer.save(content=content)
        

        
# @api_view(['GET','POST'])        
# def product_alternate_view(request,pk=None,*args,**kwargs):
#     method = request.method
    
#     if(method == "GET"):
#         if pk is not None:
#             # qs = Product.objects.filter(pk=pk)
#             # if not qs.exists():
#             #     raise Http404    
#             obj = get_object_or_404(Product,pk=pk)
#             return Response(ProductSerializer(obj,many =False).data)
#         #retirve product
        
        
#         # list_view
#         qs= Product.objects.all()
#         data = ProductSerializer(qs,many=True).data
#         return Response(data)

#     if(method=="POST"):
#         serializer = ProductSerializer(data = request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content')
            
#             if content is None:
#                 content =  title
            
#             serializer.save(content = content)   
#             return Response(serializer.data)
#             # retirve item
#         return Response({"invalid":'not_good_data'},status = 400)