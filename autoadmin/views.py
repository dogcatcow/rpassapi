import time

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from autoadmin.search import SearchEngine
from .serializers import AccountSerializer
from django.shortcuts import get_object_or_404
from .models import Account


def index(request):
    return HttpResponse("WELCOME TO AUTOADMIN ")


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def submit_account(request):
    if request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# @permission_classes((IsAuthenticated, ))
# @authentication_classes((JSONWebTokenAuthentication,))
# def question(request):



@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def change_account(request):
    if request.method == 'GET':
        change = get_object_or_404(Account, pk=1)
        list = [change.user_id, change.prev_pwd, change.new_pwd]

        engine = SearchEngine()
        engine.change(list)

        time.sleep(50)

        return HttpResponse(change.new_pwd)

