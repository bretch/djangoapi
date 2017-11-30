from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    """docstring for PersonSerializer"""
    phoneNumbers = serializers.JSONField(default=[])
    emailAddresses = serializers.JSONField(default=[])
    addresses = serializers.JSONField(default=[])

    class Meta: 
        model = Person
        fields = ('id', 'firstname', 'lastname', 'birthdate', 'phoneNumbers', 'emailAddresses', 'addresses', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')