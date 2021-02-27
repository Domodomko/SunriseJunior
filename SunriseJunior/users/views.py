from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
from .permissions import *
from .serializers import *
from .tokens import account_activation_token
from utils.services import send_mail_with_token_link
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import User
from django.http import HttpResponse
import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


class UserSignInView(APIView):
    serializer_class = UserSignInSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        email = request.data["email"]
        password = request.data["password"]
        user = authenticate(request, email=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            content = {'token': str(token.key)}
        else:
            content = {'status': "Wrong data!"}
        return Response(content)


class UserUpdateView(RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

    def get_object(self):
        return User.objects.get(pk=self.request.user.id)


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data['email']

        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_mail_with_token_link(request, 'Confirm your email', user,
                                      email, account_activation_token, 'mail/email_confirmation.html')
            return Response({'message': 'Please confirm your email address to complete the application'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return Response({'message': 'Thank you for your email confirmation.'})
    else:
        return Response({'message': 'Activation link is invalid!'})


def user_detail_view(request):
    user = request.user
    return render(request, 'users/user_profile.html', {"user": user})


def user_update_view(request):
    user = request.user
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user.first_name = first_name
        user.last_name = last_name
        user.save()
    return HttpResponse(
        json.dumps({"Nothing": "To see here!"}),
        content_type="application/json"
    )


def sign_in_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('user'))
        else:
            return HttpResponse(
                json.dumps({"Error": "No user like this"}),
                content_type="application/json"
            )
    return render(request, 'users/sign_in.html')


def sign_out_view(request):
    logout(request)
    return HttpResponse(
        json.dumps({"Success": "You are logged out!"}),
        content_type="application/json"
    )


def sign_up_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            user = User(email=email)
            user.set_password(password)
            user.is_active = False
            user.save()
            send_mail_with_token_link(request, 'Confirm your email', user,
                                      email, account_activation_token, 'mail/email_confirmation.html')
            return render(request, 'users/confirm_email.html')
        else:
            messages.warning(request, "Password don't match!")
    return render(request, 'users/sign_up.html')
