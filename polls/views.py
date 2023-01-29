from http import HTTPStatus
from datetime import datetime
from django.http import JsonResponse


def ping(request):
        data = {
            "message" : datetime.now()
        }
        return JsonResponse(data)