"""
ASGI config for spotify project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import apps.chats.routing  # đổi 'your_app' thành tên app bạn chứa ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spotify.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # vẫn hỗ trợ HTTP
    "websocket": AuthMiddlewareStack(
        URLRouter(
            apps.chats.routing.websocket_urlpatterns
        )
    ),
})
