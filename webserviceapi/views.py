from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from webserviceapi.models import Account, Post, FanRequest, Video, VideoLengthOptions, Star
from webserviceapi.serializers import AccountSerializer, PostSerializer, FanRequestSerializer, VideoLengthOptionsSerializer, VideoSerializer
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("<h1>Hello World!</h1>")


@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def star_list(request):
    """ Manipulate stars based on request

    Arguments:
        request {httpRequest} -- request from client
    """
    # GET - Retrieve list of Stars
    if request.method == 'GET':
        logger.debug('Inside Get')
        stars = Account.objects.filter(account_is_star=True)
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
@api_view(['GET', 'PUT', 'DELETE'])
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
@api_view(['POST'])
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


@csrf_exempt
@api_view(['POST'])
def user_signup(request):
    # Sign Up User based on information
    if request.method == 'POST':
        signup_data = JSONParser().parse(request)
        signup_serializer = AccountSerializer(data=signup_data)
        if signup_serializer.is_valid():
            signup_serializer.save()
            return JsonResponse(signup_serializer.data, status=status.HTTP_201_CREATED)

    return JsonResponse(signup_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # Retrieve one record
    if request.method == 'GET':
        post_serializer = PostSerializer(post)
        return JsonResponse(post_serializer.data)

    # Update one record
    if request.method == 'PUT':
        post_data = JSONParser().parse(request)
        post_serializer = AccountSerializer(post, data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data)
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete one record
    if request.method == 'DELETE':
        post.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def fanrequest_list(request):
    """ Manipulate Fan-request

    Arguments:
        request {httpRequest} -- request from client
    """
    # GET - Retrieve list of Stars
    if request.method == 'GET':
        fanrequests = FanRequest.objects.all()
        fanrequest_serializer = FanRequestSerializer(fanrequests, many=True)
        return JsonResponse(fanrequest_serializer.data, safe=False, status=status.HTTP_200_OK)

    # Add one
    if request.method == 'POST':
        fanrequest_data = JSONParser().parse(request)

        request_star_account_id = fanrequest_data['request_star_account']
        request_owner_account_id = fanrequest_data['request_owner_account']
        fanrequest_serializer = FanRequestSerializer(data=fanrequest_data)

        if fanrequest_serializer.is_valid():
            fanrequest_serializer.save(
                request_star_account=Star.objects.get(
                    pk=request_star_account_id),
                request_owner_account=Account.objects.get(
                    pk=request_owner_account_id)
            )
            return JsonResponse(fanrequest_serializer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(fanrequest_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def fanrequest_detail(request, pk):
    """Get Fan Request Details from Primary Key

    Args:
        request (HTTPRequest): HTTPRequest
        pk (number): Unique Identifier for Fan Request

    Returns:
        HTTPResponse: result of the request
    """
    try:
        fanrequest = FanRequest.objects.get(pk=pk)
    except FanRequest.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    # Retrieve one record
    if request.method == 'GET':
        fanrequest_serializer = FanRequestSerializer(fanrequest)
        return JsonResponse(fanrequest_serializer.data)

    # Update one record
    if request.method == 'PUT':
        fanrequest_data = JSONParser().parse(request)
        fanrequest_serializer = FanRequestSerializer(
            fanrequest, data=fanrequest_data)
        if fanrequest_serializer.is_valid():
            fanrequest_serializer.save()
            return JsonResponse(fanrequest_serializer.data)
        return JsonResponse(fanrequest_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete one record
    if request.method == 'DELETE':
        fanrequest.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
