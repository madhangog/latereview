# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . serializer import AudienceSerializer
from . models import Audience

from django.core.signing import Signer
from rest_framework.parsers import JSONParser


signer = Signer()



# from .forms import RegisterFrom

# Create your views here.

# def index(request):
# 	return HttpResponse("<h1> Heloio </h1>")

# def register(request):
	# if request.method == 'POST':
	   #  form = RegisterFrom(request.POST)
	   #  if form.is_valid():
	   #      pass  # does nothing, just trigger the validation
	# else:
	#     form = RegisterFrom()
	# return render( request ,"users/register.html", {'form': form})
	# return HttpResponse("hello")

class UserList(APIView):
	@classmethod
	def hash_password(cls,password):
		signer = Signer()
		value = signer.sign(password)
		print value
		return value

	def get(self, request ,format=None):
		usersData = Audience.objects.all()
		serializer = AudienceSerializer(usersData, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = AudienceSerializer(data=request.data)
		if serializer.is_valid():
			data = serializer.validated_data
			print(data)
			password = data['password']
			print(password)
			dbpass = self.hash_password(password)
			print(dbpass)
			serializer.validated_data['password'] = dbpass
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):

	parser_classes = (JSONParser,)

	def post(self, request, format=None):
		username = request.data["username"]
		password = request.data["password"]
		print username
		print password
		try:
			usersData = Audience.objects.get(username = username)
			original_password = signer.unsign(usersData.password)
			if password == original_password:
				request.session['user_id'] = usersData.user_id

				return HttpResponse("Logged in successfully")
			else:
				return HttpResponse("incorrect password ")
		except Audience.DoesNotExist:
			return HttpResponse("Username and password not matched!")
			# return Response({'received data': request.data})
class Logout(APIView):

	def get(self,request):
		try:
			del request.session['user_id']
		except KeyError:
			pass #return #HttpResponse('already logged out . log in and try again ')
		return HttpResponse("You're logged out.")

class CheckLogin(APIView):
	def get(self, request):
		try:
			id_in_session = request.session['user_id']
			usersData = Audience.objects.get(user_id = id_in_session)
			return HttpResponse(' uset {0} logged in already'.format(usersData.username))
		except KeyError:
			return HttpResponse('already logged out . log in and try again ')