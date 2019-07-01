# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import  Movies
from . serializer import MoviesSerializer
from rest_framework.parsers import JSONParser

# Create your views here.

class MovieList(APIView):

	def post(self, request, format = None):
		serializer = MoviesSerializer(data=request.data)
		if serializer.is_valid():
			data = serializer.validated_data
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, format= None):
		try:
			request.session['critic_id']
			try:
				MovieData = Movies.objects.all()
				print MovieData
				serializer = MoviesSerializer(MovieData, many=True)
				return Response(serializer.data)
			except: 
				return HttpResponse("error in getting objects")
		except KeyError: 
			return HttpResponse("not logged into admin account")


