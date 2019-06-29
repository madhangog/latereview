from rest_framework import serializers
from . models import Audience
from . models import Critics


class AudienceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Audience
		# fields = ('user_id' , 'username', 'password', 'mobile')
		fields = '__all__'


class CriticsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Critics
		# fields = ('user_id' , 'username', 'password', 'mobile')
		fields = '__all__'

 