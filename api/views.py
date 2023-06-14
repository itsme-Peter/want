from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,generics
from . import serializers
from django.shortcuts import get_object_or_404
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated

from safety_wear import models

# Create your views here.
@api_view(["GET"])
def all(request):

    instance = models.products.objects.all().order_by("?").last()
    data = {}
    if instance:
        data = serializers.productSerializer(instance).data
    return Response(data)

@api_view(["POST"])
def add(request):   
    data = {}
    
    serializer = serializers.productSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.data
        return Response(data)
    return Response({"invalid":"not good data"},status=400)

@api_view(["GET","POST"])
def product_alt(request,pk=None,*args,**kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(models.products,pk)
            data = serializers.productSerializer(obj).data
            return Response(data)    
        queryset = models.products.objects.all()
        data = serializers.productSerializer(queryset,many=True).data
        print(data)
        return Response(data)
        
    if method == "POST":        
        serializer = serializers.productSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            return Response(data)
        return Response({"invalid":"not good data"},status=400)


class productDetail(generics.RetrieveAPIView):
    queryset = models.products.objects.all()
    serializer_class = serializers.productSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,

    ]

class list_create(generics.ListCreateAPIView):
    queryset = models.products.objects.all()
    serializer_class = serializers.productSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,

    ]
    
    def perform_create(self, serializer):
        serializer.save()
        return()

product_detail = productDetail.as_view()
list_created = list_create.as_view()
