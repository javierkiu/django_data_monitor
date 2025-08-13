from django.shortcuts import render
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse

@login_required
def index(request):

    response = requests.get(settings.API_URL) 
    posts = response.json() 

    print (type(posts))

    total_responses = len(posts)

    order_sum = 0
    dproductos = {}
    dordenes_fechas = {}
    for order_id, order_info in posts.items():
        order_sum += order_info['total']
        if order_info['timestamp'][:10] in dordenes_fechas:
            dordenes_fechas[order_info['timestamp'][:10]] += 1
        else:
            dordenes_fechas[order_info['timestamp'][:10]] = 1

        for item_id, item_info in order_info['items'].items():
            if item_info['name'] in dproductos:
                dproductos[item_info['name']] += item_info['quantity']
            else:
                dproductos[item_info['name']] = item_info['quantity']
        
    order_average = order_sum / total_responses if total_responses > 0 else 1
    max_product = max(dproductos, key=dproductos.get)
    products = sorted(dproductos.items(), key=lambda x: x[1], reverse=True)
    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,
        'order_average': round(order_average, 2), 
        'max_product': max_product,
        'orser_sum': round(order_sum, 2),
        'products': products,
        'dordenes_fechas': dordenes_fechas,
    }
    
    return render(request, 'dashboard/index.html', data)