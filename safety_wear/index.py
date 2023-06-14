from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import products

@register(products)

class productsIndex(AlgoliaIndex):
    fields = [
        "user",
        "name",
        "description",
        "price",
        "category",
        "available",
        "image"
    ]