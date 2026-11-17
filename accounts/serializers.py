from accounts.models import CustumUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustumUser
        fields=['username','password','email','phone_no','bio']

    def create(self,validated_data):
        u=CustumUser.objects.create_user(**validated_data)
        u.save()
        return u