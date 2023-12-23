import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from oauth2_provider.settings import oauth2_settings
from braces.views import CsrfExemptMixin
from oauth2_provider.views.mixins import OAuthLibMixin

import json
from users import models, serializers

from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.translation import gettext_lazy as _
from django.db import transaction
from django.conf import settings


class Login(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        request_data = request.data
        try:
            email = request_data.get('email')
            password = request_data.get('password')
            user_details = models.User.objects.filter(email=email)
            if user_details:
                url = request.build_absolute_uri('/o/token/')
                r = requests.post(url, data={'grant_type': 'password',  # your defined grant type
                                             'client_id': settings.OAUTH_CLIENT_ID,  # your clinet id
                                             'client_secret': settings.OAUTH_CLIENT_SECRET,  # your client secret
                                             'username': user_details[0].username,  # your username that you get from user
                                             'password': password,  # your password that you get from user
                                             'redirect_uri': request.build_absolute_uri('/menu')
                                             }
                                  )
                print(r.status_code)
                return Response(r.json())
            else:
                return Response(json.loads('{"message": "User does not exists."}'))
        except Exception as e:
            error = {"message": e.__str__()}
            return Response(json.loads(json.dumps(error)))


class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        data = request.data
        data = data.dict()
        serializer = serializers.RegisterSerializer(data=data)
        if serializer.is_valid():
            try:
                with transaction.atomic():
                    serializer.save()
                    return Response(json.loads('{"message": "registration successful"}'), status=status.HTTP_200_OK)
            except Exception as e:
                return Response(data={"error": e.__str__()}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Check(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return Response(json.loads('{"message": "Authenticated !"}'), status=status.HTTP_200_OK)
