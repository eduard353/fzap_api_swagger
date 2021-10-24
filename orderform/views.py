from django.shortcuts import render
from .models import Order, Mark, Model, Shop, Answer
from .forms import OrderForm, MarkForm
from django.http import JsonResponse
from .serializers import MarkSerializer, ModelSerializer, OrderSerializer, ShopSerializer, AnswerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.decorators import action


# Create your views here.

def OrdersListView(request):
    """ Представление списка заказов """
    orders_list = Order.objects.all()

    return render(request, 'orders_list.html', {'orders': orders_list})

class MarksViewSet(viewsets.ModelViewSet):
    """API представление всех Марок автомобилей"""
    serializer_class = MarkSerializer
    queryset = Mark.objects.all()


class ModelsViewSet(viewsets.ModelViewSet):
    """API представление Моделей автомобилей определенной Марки"""
    serializer_class = ModelSerializer
    queryset = Model.objects.all()


class OrdersViewSet(viewsets.ModelViewSet):
    """API представление всех Заказов"""
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

class ShopsViewSet(viewsets.ModelViewSet):
    """API представление всех Магазинов"""
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
    # queryset = Shop.objects.all()

class AnswersViewSet(viewsets.ModelViewSet):
    """API представление всех Ответов"""
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

