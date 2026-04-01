from django.shortcuts import render
from django.http import JsonResponse
from .models import Product, Category

def product_list(request):
    products=Product.objects.all()
    data=[
        {
        "id": p.id,
        "name": p.name,
        "price": p.price,
        "description": p.description,
        "count": p.count,
        "is_active": p.is_active,
        "category_id": p.category.id
        }
        for p in products
    ]
    return JsonResponse(data, safe=False)

def product_detail(request, id):
    try:
        p =Product.objects.get(id=id)
        data={
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "description": p.description,
            "count": p.count,
            "is_active": p.is_active,
            "category_id": p.category.id
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({"error":"Not found"})

def category_list(request):
    categories=Category.objects.all()
    data=[
    {
        "id": c.id, 
        "name": c.name
        } 
    for c in categories]
    return JsonResponse(data, safe=False)

def category_detail(request, id):
    try:
        c=Category.objects.get(id=id)
        data={
            "id": c.id, 
            "name": c.name
        }
        return JsonResponse(data)
    except Category.DoesNotExist:
        return JsonResponse({"error":"Not found"})

def category_products(request, id):
    try:
        category=Category.objects.get(id=id)
        products=category.products.all()
        data=[
        {
        "id": p.id,
        "name": p.name,
        "price": p.price,
        "description": p.description,
        "count": p.count,
        "is_active": p.is_active,
        "category_id": p.category.id
        }
        for p in products
    ]
        return JsonResponse(data, safe=False)
    except Category.DoesNotExist:
        return JsonResponse({"error":"Not found"})
      

def product_sort(request):
    products=Product.objects.order_by("count")
    data=[
        {
        "id": p.id,
        "name": p.name,
        "price": p.price,
        "description": p.description,
        "count": p.count,
        "is_active": p.is_active,
        "category_id": p.category.id
        }
        for p in products
    ]
    return JsonResponse(data, safe=False)











    #JsonResponse data   
 #filter
 #.get(id=id)
 #all()
 #gt- > something__gt=50
 #lt <
#order_by something (минус для убыван)
#[:3] + олка