# your_project/routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from EC2 import ec2_consumers
from inventory import inventory_consumers

websocket_urlpatterns = [
    path('ws/ec2/', ec2_consumers.EC2Consumer.as_asgi()),
    path('ws/inventory/', inventory_consumers.InventoryConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(
        websocket_urlpatterns
    ),
    # (http->django views is added by default)
})


# # myproject/routing.py

# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack
# from django.urls import path, include

# application = ProtocolTypeRouter({
#     # (http->django views is added by default)
#     'websocket': AuthMiddlewareStack(
#         URLRouter([
#             path('ec2/', include('ec2.routing.websocket_urlpatterns')),
#             path('inventory/', include('inventory.routing.websocket_urlpatterns')),
#             # Include other app routing here
#         ])
#     ),
# })