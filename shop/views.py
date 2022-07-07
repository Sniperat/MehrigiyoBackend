from django.conf import settings
from django.db.models import Avg
from django.shortcuts import render
from drf_yasg import openapi
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .filters import ProductFilter
from account.models import DeliveryAddress
from config.responses import ResponseSuccess, ResponseFail
from .serializers import (TypeMedicineSerializer, MedicineSerializer, CartSerializer, OrderCreateSerializer,
                          OrderShowSerializer, AdvertisingSerializer, ListSerializer)
from .models import PicturesMedicine, TypeMedicine, Medicine, CartModel, OrderModel, Advertising
from rest_framework import viewsets, generics
from drf_yasg.utils import swagger_auto_schema
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet


class AdvertisingView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        types = Advertising.objects.all()
        serializer = AdvertisingSerializer(types, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)


class TypeMedicineView(viewsets.ModelViewSet):
    queryset = TypeMedicine.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = TypeMedicineSerializer

    def get(self, request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return ResponseSuccess(data=self.get_paginated_response(serializer.data), request=request.method)


class MedicinesView(ListModelMixin, GenericViewSet):
    queryset = Medicine.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = MedicineSerializer
    filterset_class = ProductFilter

    # @swagger_auto_schema(manual_parameters=[
    #     openapi.Parameter('key', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_STRING)
    # ])
    # def get_serializer_context(self):
    #     return self.request

    def get(self, request):
        # key = request.GET.get('key', False)
        # queryset = self.queryset

        # if key:
        #     queryset = self.queryset.filter(name__contains=key)
        # serializer = self.get_serializer(queryset, many=True)
        queryset = self.queryset.annotate(
            total_rate=Avg('comments_med__rate')
        )
        filtered_qs = self.filterset_class(request.GET, queryset=queryset).qs
        print(filtered_qs)

        page = self.paginate_queryset(filtered_qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'user': request.user})
            return ResponseSuccess(data=self.get_paginated_response(serializer.data), request=request.method)
        # return ResponseSuccess(data=serializer.data, request=request.method)


class GetMedicinesWithType(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = MedicineSerializer

    @action(detail=True, methods=['post'])
    def get_with_types(self, request, *args, **kwargs):
        print(request.data['list']+'---------')
        id_list = list(request.data['list'].split(','))
        medicine = Medicine.objects.filter(type_medicine_id__in=id_list)
        page = self.paginate_queryset(medicine)
        if page is not None:
            serializer = self.get_serializer(page, many=True, context={'user': request.user})
            return ResponseSuccess(data=self.get_paginated_response(serializer.data), request=request.method)


class GetSingleMedicine(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    # permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('pk', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_STRING)
    ])
    def get(self, request):

        key = request.GET.get('pk', False)
        queryset = self.queryset

        if key:
            queryset = self.queryset.filter(name__contains=key)
        serializer = self.get_serializer(queryset, context={'user': request.user})
        return ResponseSuccess(data=serializer.data, request=request.method)


class CartView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        carts = CartModel.objects.filter(user=request.user, status=1)
        serializer = CartSerializer(carts, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)

    def post(self, request):
        serializer = CartSerializer(data=request.data, context={'request': request})
        med = Medicine.objects.get(id=request.data['product'])
        if serializer.is_valid():
            cart = CartModel.objects.create(user=request.user, product=med)
            # serializer.save()
            serializer = CartSerializer(cart)
            return ResponseSuccess(data=serializer.data, request=request.method)
        else:
            return ResponseFail(data=serializer.errors, request=request.method)

    def put(self, request):
        cart = CartModel.objects.get(id=request.data['id'], user=request.user)
        del request.data['id']
        serializer = CartSerializer(cart, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(data=serializer.data, request=request.method)
        else:
            return ResponseFail(data=serializer.errors, request=request.method)

    def delete(self, request):
        try:
            CartModel.objects.get(id=request.data['id'], user=request.user).delete()
            return ResponseSuccess(request=request.method)
        except:
            return ResponseFail(request=request.method)


class OrderView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        orders = OrderModel.objects.filter(user=request.user)
        serializer = OrderShowSerializer(orders, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)

    def post(self, request):
        carts = CartModel.objects.filter(user=request.user, status=1)
        order = OrderModel()
        order.user = request.user
        order.save()
        summa = 0
        for i in carts:
            order.cart_products.add(i)
            summa += i.get_total_price
            i.status = 2
            i.save()
        order.price = summa
        order.save()
        serializer = OrderShowSerializer(order)
        return ResponseSuccess(data=serializer.data, request=request.method)

    def put(self, request):
        try:
            order = OrderModel.objects.get(id=request.data['id'])
        except:
            return ResponseFail(data='Order not found')
        try:
            id = request.data['shipping_address']
            da = DeliveryAddress.objects.get(id=id)
            add_key = 1
        except:
            add_key = 0
        del request.data['id']
        serializer = OrderCreateSerializer(order, data=request.data)
        if serializer.is_valid():
            if add_key == 1:
                if order.shipping_address is None:
                    if da.region.delivery_price == 0:
                        order.price = order.price + settings.DEFAULT_DELIVERY_COST
                    else:
                        order.price = order.price + da.region.delivery_price
                else:
                    old_price = order.shipping_address.region.delivery_price
                    print(old_price)
                    if old_price == 0:
                        order.price = order.price - settings.DEFAULT_DELIVERY_COST
                        print('1')
                    else:
                        order.price = order.price - old_price
                    if da.region.delivery_price == 0:
                        order.price = order.price + settings.DEFAULT_DELIVERY_COST
                    else:
                        order.price = order.price + da.region.delivery_price
            order.save()
            serializer.save()
            serializer = OrderShowSerializer(order)
            return ResponseSuccess(data=serializer.data, request=request.method)
        else:
            return ResponseFail(data=serializer.errors, request=request.method)

