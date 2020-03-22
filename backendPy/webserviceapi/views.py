from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from backendPy.webserviceapi.models import User, Star
from backendPy.webserviceapi.serializers import UserSerializer, StarSerializer

# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello World!</h1>")


@csrf_exempt
def star_list(request):
    """ Manipulate stars based on request

    Arguments:
        request {httpRequest} -- request from client
    """
    # GET - Retrieve list of Stars
    if request.method == 'GET':
        stars = Star.objects.all()
        stars_serializer = StarSerializer(stars, many=True)
        return JsonResponse(stars_serializer.data, safe=False, status=status.HTTP_200_OK)


@csrf_exempt
def star_detail(request, pk):
    """Manipulate one star based on request

    Arguments:
        request {HttpRequest} -- request from client
        pk {identifier} -- Primary Key

    Returns:
        JSONResponse -- Result after operation
    """
    # getStar from Primary Key
    try:
        star = Star.objects.get(pk=pk)
    except Star.DoesNotExist as notfound:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

     # GET - Retrieve one record
    if request.method == 'GET':
        star_serializer = StarSerializer(star)
        return JsonResponse(star_serializer.data, status=status.HTTP_200_OK)
