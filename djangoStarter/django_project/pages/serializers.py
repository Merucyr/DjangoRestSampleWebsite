from rest_framework import serializers
from .models import NewAPIPerson

class NewAPIPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewAPIPerson
        fields = '__all__'