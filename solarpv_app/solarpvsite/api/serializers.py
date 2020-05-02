from rest_framework import serializers
from ..models import Product, Certificate, Service, Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['clientCode', 'clientName', 'clientType']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['modelnum', 'name', 'manufacturer']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['certid', 'userID', 'reportnum']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['serviceid', 'servicename', 'description']
