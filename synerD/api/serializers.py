from rest_framework import serializers
from ..models import Subscriber, Service, Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['organization_code','organization_name','description',\
                'date_joined','address1','address2','city','state','zipcode',\
                'phone_number']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['servicecode','servicename','description','premium','allocation']

class SubscriberSerializer(serializers.ModelSerialiser):
    class Meta:
        model = Subscriber
        fields = ['requestdate','startdate','enddate','motifofcancellation', \
                'beneficiaryID','subscriberID','username','subscriptiontypecode', \
                'servicecode']


