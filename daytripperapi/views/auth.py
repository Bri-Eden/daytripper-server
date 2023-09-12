from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from daytripperapi.models import Planner


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles the authentication of a gamer

    Method arguments:
      request -- The full HTTP request object
    '''
    username = request.data['username']
    password = request.data['password']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    authenticated_user = authenticate(username=username, password=password)

    # If authentication was successful, respond with their token
    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        data = {
            'valid': True,
            'token': token.key
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = {'valid': False}
        return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new gamer for authentication

    Method arguments:
      request -- The full HTTP request object
    '''
    email=request.data.get('email', None)
    first_name = request.data.get('first_name', None)
    last_name = request.data.get('last_name', None)
    password = request.data.get('password', None)
    location = request.data['location']
    photo = request.data['photo']

    if email is not None\
            and first_name is not None \
            and last_name is not None \
            and password is not None:
    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
        try:
                
            new_user = User.objects.create_user(
                username=request.data['email'],
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            # Now save the extra info in the levelupapi_gamer table
            planner = Planner.objects.create(
                location=location,
                photo=photo,
                user=new_user
            )
        
        except IntegrityError:
            return Response(
                {'message': 'An account with that email already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )

    # Use the REST Framework's token generator on the new user account
        token = Token.objects.create(user=planner.user)
        # Return the token to the client
        data = {'token': token.key}
        return Response(data)
    return Response({'message': 'You must provide email, password, first_name, and last_name'}, status=status.HTTP_400_BAD_REQUEST)
