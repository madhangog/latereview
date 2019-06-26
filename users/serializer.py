from rest_framework import serializers
from . models import Audience

class AudienceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Audience
		# fields = ('user_id' , 'username', 'password', 'mobile')
		fields = '__all__'

 