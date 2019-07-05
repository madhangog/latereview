from rest_framework import serializers
from . models import Audience, Critics#, reviewer
# from rest_polymorphic.serializers import PolymorphicSerializer



# class reviewerSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = reviewer
# 		# fields = ('user_id' , 'username', 'password', 'mobile')
# 		fields = '__all__'

 

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


# class reviewerPolymorphicSerializer(PolymorphicSerializer):

# 		model_serializer_mapping = {
# 			reviewer: reviewerSerializer,
# 			Audience: AudienceSerializer,
# 			Critics: CriticsSerializer
# 		}


#  