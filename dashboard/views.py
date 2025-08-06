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
    # for order_id, order_info in posts.items():
    #     print(f"ID de Orden: {order_id}")
    #     print(f"Fecha de la orden: {order_info['timestamp']}")
    #     print(f"Total de la orden: ${order_info['total']}")
        
    #     # Recorrer los items de cada orden
    #     for item_id, item_info in order_info['items'].items():
    #         print(f"  - Producto: {item_info['name']}")
    #         print(f"    Imagen: {item_info['image']}")
    #         print(f"    Precio: {item_info['price']}")
    #         print(f"    Cantidad: {item_info['quantity']}")
        
    #     print("\n" + "-"*50 + "\n")

    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,
    }
    
    return render(request, 'dashboard/index.html', data)