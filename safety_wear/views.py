from django.shortcuts import render,get_object_or_404
from . import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import productSerializer,feedbackSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.core.mail import send_mail


# Create your views here.
qs = models.products.objects.all()
qs = productSerializer(qs,many=True).data


def categories():
    cats = []
    category_name={}
    for i in range(0,len(qs)):
        category = qs[i]["category"]
        if category not in cats:
            cats.append(category)
            category_name[category] = []
        category_name[category].append(qs[i]["name"]) 
    return category_name


def sending_emails():
    send_mail(
    'Trial',
    'This is a trial email to myself',
    'safetyNairobiWear.co.ke',
    ['lamphilosopher101@gmail'],
    fail_silently=False,
        )
    return Response("Sent successfully")

## a simplified version
def send_email(subject,message,rec,to):
    send_mail(subject,message,rec,to,fail_silently=False,)

def index(request):  
    context = {
        'category_name':categories()
    }     
    return render(request,"safetyIndex.html", context)

def productsPage(request):
    context = {
        'category_name':categories()
    } 
    return render(request,"products.html",context)

class ProductPagination(PageNumberPagination):
    page_size = 16
    page_size_query_param = 'page_size'
    max_page_size = 16

    def get_paginated_response(self, data):
        page_size = self.page_size
        pages = self.page.paginator.count//page_size + 1
        return Response({
            'count': self.page.paginator.count,
            'pages': pages,
            'page_number': self.page.number,
            'page_size': page_size,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })

class all(generics.ListCreateAPIView):
    queryset = models.products.objects.all()
    serializer_class = productSerializer
    pagination_class = ProductPagination

class the_Product(generics.RetrieveAPIView):     
    queryset = models.products.objects.all()
    serializer_class = productSerializer
    pk = 'pk'

class randomProducts(generics.ListAPIView):
    serializer_class = productSerializer
    pagination_class = ProductPagination
    # page_size = 5
    # page_size_query_param = 'page_size'
    # max_page_size = 10
    
    def get_queryset(self):
        return models.products.objects.all().order_by("?")[:12]
    

def theProduct(request,name):
    product = get_object_or_404(models.products,name=name)
    product = productSerializer(product).data

    product_id = product["id"]
    context = {
        'product_id':product_id,
        'category_name':categories(),
    }
    return render(request,"product.html",context)

@api_view(['GET'])
def byCategory(request,name):
    products = models.products.objects.filter(category=name)
    if products:
        products = productSerializer(products,many=True).data
        return Response(products,status=200)
    else:
        return Response({"error":"no products found"},status=404)

def by(request,name):
    products = models.products.objects.filter(category=name)
    lens = 0
    print(len(products))
    if products:
        products = productSerializer(products,many=True).data
        for product in products:
            product["image"] = product["image"].split("?")[0].replace('https://iwantmainbucket.s3.amazonaws.com', 'https://d3pvj3ro00vroz.cloudfront.net')
            print(product["image"])
    context = {
        "products":products,
        "name":name.capitalize(),
        "lens":len(products),
        'category_name':categories(),
    }
    return render(request,"by.html",context)
@api_view(["POST"])
def feedback(request):
    data=request.data
    print(data)
    serializer = feedbackSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({"success":"Sent successfully"})
    return Response({"invalid":"not good data"},status=400)


randoms = randomProducts.as_view()
allProducts = all.as_view()
product = the_Product.as_view()
