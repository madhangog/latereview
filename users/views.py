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

	def get(self, request ,format=None):
		usersData = Audience.objects.all()
		serializer = AudienceSerializer(usersData, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
    		serializer = AudienceSerializer(data=request.data)
	        if serializer.is_valid():
	            serializer.save()
	            return Response(serializer.data, status=status.HTTP_201_CREATED)
	        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
