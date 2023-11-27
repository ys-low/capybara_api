from rest_framework import serializers
from api.models import Capybara, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields=('name','longitude','latitude')

class ListCapySerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    class Meta:
        model=Capybara
        fields=('id','name','gender','slug','image_url','summary','location')

class DetailCapySerializer(serializers.ModelSerializer):
    class Meta:
        model=Capybara
        fields=('id','name','gender','birthday','slug','image_url','description')
