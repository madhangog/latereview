from rest_framework import serializers
from . models import Movies

class MoviesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movies
		# fields = ('user_id' , 'username', 'password', 'mobile')
		fields = '__all__'
