from django.http import JsonResponse
from products.models import Product
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    # instance = Product.objects.all().order_by("?").first()
    # instance = request.data
    # data ={}
    
    # if instance:
    #         data = ProductSerializer(instance).data
    
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)
    
    return Response({"invalid":"Data is invalid"})