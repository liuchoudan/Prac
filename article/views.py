from django.http import HttpResponse
from .models import Student


def test(request):

    return HttpResponse('Hello World!')
