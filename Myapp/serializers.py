from .models import *
from rest_framework import serializers

class roomserializers(serializers.ModelSerializer):
    # chairperson = serializers.SlugField(slug_field='name', chairperson.objects.all())

    class Meta:
        model=Room
        fields = '__all__'
        
class studentserializers(serializers.ModelSerializer):
    # chairperson = serializers.SlugField(slug_field='name', chairperson.objects.all())

    class Meta:
        model=Student
        fields = '__all__'
        
class paymentserializers(serializers.ModelSerializer):
    # chairperson = serializers.SlugField(slug_field='name', chairperson.objects.all())

    class Meta:
        model=Payment
        fields = '__all__'
        
class complaintserializers(serializers.ModelSerializer):
    # chairperson = serializers.SlugField(slug_field='name', chairperson.objects.all())

    class Meta:
        model=Complaint
        fields = '__all__'