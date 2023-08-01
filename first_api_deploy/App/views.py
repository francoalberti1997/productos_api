from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductoSerializer
from .models import Producto
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def productos(request, *args, **kwargs):
    if request.method == "GET":
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many = True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer =  ProductoSerializer(data = request.data, many = True)
        if serializer.is_valid():
            product = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    