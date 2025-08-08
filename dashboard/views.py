from django.shortcuts import render
import requests
from django.conf import settings

# Create your views here.
from django.http import HttpResponse

def index(request):

    response = requests.get(settings.API_URL)  # URL de la API
    posts = response.json()  # Convertir la respuesta a JSON

    print (type(posts))

    # Número total de respuestas
    total_responses = len(posts)
    order_sum = 0
    dproductos = {}
    for order_id, order_info in posts.items():
        order_sum += order_info['total']
        # Recorrer los items de cada orden
        for item_id, item_info in order_info['items'].items():
            if item_info['name'] in dproductos:
                dproductos[item_info['name']] += item_info['quantity']
            else:
                dproductos[item_info['name']] = item_info['quantity']
        
    order_average = order_sum / total_responses if total_responses > 0 else 1
    max_product = max(dproductos, key=dproductos.get)
    top10_products = sorted(dproductos.items(), key=lambda x: x[1], reverse=True)[:10]
    print(top10_products)
    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,
        'order_average': round(order_average, 2), 
        'max_product': max_product,
        'orser_sum': round(order_sum, 2),
        'top10_products': top10_products,
    }
    
    return render(request, 'dashboard/index.html', data)