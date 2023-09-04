from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django_filters import rest_framework as filters
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import TransactionSerializer, UserSerializer
from .models import Transaction


class TransactionFilter(filters.FilterSet):
    min_amount = filters.NumberFilter(field_name='amount', lookup_expr='gte')
    max_amount = filters.NumberFilter(field_name='amount', lookup_expr='lte')
    start_date = filters.NumberFilter(field_name='date', lookup_expr='gte')
    end_date = filters.NumberFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Transaction
        fields = ['min_amount', 'max_amount', 'start_date', 'end_date']


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('-date')
    serializer_class = TransactionSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TransactionFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


@api_view(['POST'])
def register(request):
    if request.method == "POST":
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)


@require_POST
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        # login succeed
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'message': 'User Not Found'}, status=400)
