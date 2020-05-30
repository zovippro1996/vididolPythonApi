from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from backendPy.webserviceapi.models import Account
from backendPy.webserviceapi.serializers import AccountSerializer
from django.contrib.auth import authenticate, login


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
        stars = Account.objects.get(account_is_star=True)
        star_serializer = AccountSerializer(stars, many=True)
        return JsonResponse(star_serializer.data, safe=False, status=status.HTTP_200_OK)

    # Add one
    if request.method == 'POST':
        star_data = JSONParser().parse(request)
        star_serializer = AccountSerializer(data=star_data)
        if star_serializer.is_valid():
            star_serializer.save()
            return JsonResponse(star_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(star_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        Account.objects.get(account_is_star=True).delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def star_detail(request, pk):
    try:
        star = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # Retrieve one record
    if request.method == 'GET':
        star_serializer = AccountSerializer(star)
        return JsonResponse(star_serializer.data)

    # Update one record
    if request.method == 'PUT':
        star_data = JSONParser().parse(request)
        star_serializer = AccountSerializer(star, data=star_data)
        if star_serializer.is_valid():
            star_serializer.save()
            return JsonResponse(star_serializer.data)
        return JsonResponse(star_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete one record
    if request.method == 'DELETE':
        star.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def user_signin(request):
    # Sign In with Username and Password
    if request.method == 'POST':
        signin_data = JSONParser().parse(request)
        signin_serializer = AccountSerializer(data=signin_data)
        if signin_serializer.is_valid():
            validUser = authenticate(
                username=signin_serializer.data.username,
                password=signin_serializer.data.username
            )

            if validUser is not None:
                login(request, validUser)
                return JsonResponse(status=status.HTTP_200_OK)
            else:
                return JsonResponse(status=status.HTTP_401_UNAUTHORIZED)

        return JsonResponse(signin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
