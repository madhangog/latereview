from rest_framework import serializers
from . models import Movies, Reviews

class MoviesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movies
		# fields = ('user_id' , 'username', 'password', 'mobile')
		fields = '__all__'

class ReviewsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reviews
		# fields = ('user_id' , 'username', 'password', 'mobile')
		fields = '__all__'
