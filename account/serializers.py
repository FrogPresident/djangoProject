from django.contrib.auth.models import User
from rest_framework import serializers
from account.models import Transaction, Tag


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        # fields = '__all__'
        fields = ['id', 'date', 'description', 'tag', 'transaction_type', 'amount', 'user']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
