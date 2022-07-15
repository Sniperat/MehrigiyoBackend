from django.conf import settings
from django.db.models import Avg
from django.shortcuts import render
from drf_yasg import openapi
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from .filters import ProductFilter
from account.models import DeliveryAddress
from config.responses import ResponseSuccess, ResponseFail
from .serializers import (TypeMedicineSerializer, MedicineSerializer, CartSerializer, OrderCreateSerializer,
                          OrderShowSerializer, AdvertisingSerializer, ListSerializer, CartPostSerializer,
                          PutSerializer)
from .models import PicturesMedicine, TypeMedicine, Medicine, CartModel, OrderModel, Advertising
from rest_framework import viewsets, generics
from drf_yasg.utils import swagger_auto_schema
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet


class AdvertisingShopView(generics.ListAPIView):
    queryset = Advertising.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = AdvertisingSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    @swagger_auto_schema(
        operation_id='advertising',
        operation_description="advertisingView",
        # request_body=AdvertisingSerializer(),
        responses={
            '200': AdvertisingSerializer()
        },
    )
    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs)


class TypeMedicineView(viewsets.mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = TypeMedicine.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = TypeMedicineSerializer

    @swagger_auto_schema(
        operation_id='get_medicines_types',
        operation_description="get_medicines_types",
        request_body=TypeMedicineSerializer(),
        responses={
            '200': TypeMedicineSerializer()
        },
        # method='get'
        # permission_classes=[IsAuthenticated, ],
        # tags=['photos'],
    )
    def get(self, request):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return ResponseSuccess(data=self.get_paginated_response(serializer.data), request=request.method)


class MedicinesView(generics.ListAPIView):
    queryset = Medicine.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = MedicineSerializer
    filterset_class = ProductFilter

    @swagger_auto_schema(
        operation_id='get_doctors',
        operation_description="get_doctors",
        # request_body=DoctorSerializer(),
        responses={
            '200': MedicineSerializer()
        },
        # method='get'
        # permission_classes=[IsAuthenticated, ],
        # tags=['photos'],
    )
    def get(self, request, *args, **kwargs):
        queryset = self.queryset.annotate(
            total_rate=Avg('comments_med__rate')
        )
        filtered_qs = self.filterset_class(request.GET, queryset=queryset).qs
        self.queryset = filtered_qs
        print('333333333333')

        return self.list(request, *args, **kwargs)
    # def get(self, request):
    #     # key = request.GET.get('key', False)
    #     # queryset = self.queryset
    #
    #     # if key:
    #     #     queryset = self.queryset.filter(name__contains=key)
    #     # serializer = self.get_serializer(queryset, many=True)
    #     queryset = Medicine.objects.annotate(
    #         total_rate=Avg('comments_med__rate')
    #     )
    #     filtered_qs = self.filterset_class(request.GET, queryset=queryset).qs
    #     print(filtered_qs)
    #
    #     page = self.paginate_queryset(filtered_qs)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return ResponseSuccess(data=self.get_paginated_response(serializer.data), request=request.method)
    #     # return ResponseSuccess(data=serializer.data, request=request.method)

    def get_serializer_context(self):
        context = super(MedicinesView, self).get_serializer_context()
        context.update({'user': self.request.user})
        return context


class GetMedicinesWithType(generics.ListAPIView):
    queryset = Medicine.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = MedicineSerializer

    @swagger_auto_schema(
        # request_body=DoctorSerializer(),
        manual_parameters=[
            openapi.Parameter('type_ides', openapi.IN_QUERY, description="test manual param",
                              type=openapi.TYPE_STRING)
        ], operation_description='GET /articles/today/')
    @action(detail=False, methods=['get'])
    def get(self, request, *args, **kwargs):
        key = request.GET.get('type_ides', False)
        if key:
            keys = key.split(',')
            self.queryset = self.queryset.filter(type_medicine_id__in=keys)
        return self.list(request, *args, **kwargs)


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
    serializer_class = CartSerializer

    @swagger_auto_schema(
        operation_id='get_Cart',
        operation_description="get_Cart",
        responses={
            '200': CartSerializer()
        },

    )
    def get(self, request):
        carts = CartModel.objects.filter(user=request.user, status=1)
        serializer = CartSerializer(carts, many=True, context={'request': request, 'user': request.user})
        return ResponseSuccess(data=serializer.data, request=request.method)

    @swagger_auto_schema(
        operation_id='create_Cart',
        operation_description="send 'product' = id product",
        request_body=CartPostSerializer(),
        responses={
            '200': CartSerializer()
        },

    )
    def post(self, request):
        print('asdasd')
        serializer = CartSerializer(data=request.data, context={'request': request,
                                                                'user': request.user})
        med = Medicine.objects.get(id=request.data['product'])
        if serializer.is_valid():
            cart = CartModel.objects.create(user=request.user, product=med)

            # serializer.save()
            serializer = CartSerializer(cart, context={'request': request, 'user': request.user})
            return ResponseSuccess(data=serializer.data, request=request.method)
        else:
            return ResponseFail(data=serializer.errors, request=request.method)

    @swagger_auto_schema(
        operation_id='update_Cart',
        operation_description="UpdateCart",
        request_body=PutSerializer(),
        responses={
            '200': CartSerializer()
        },

    )
    def put(self, request):
        cart = CartModel.objects.get(id=request.data['id'], user=request.user)
        del request.data['id']
        serializer = CartSerializer(cart, data=request.data, context={'request': request,
                                                                      'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(data=serializer.data, request=request.method)
        else:
            return ResponseFail(data=serializer.errors, request=request.method)

    @swagger_auto_schema(
        operation_id='delete_Cart',
        operation_description="DeleteCart",
        request_body=PutSerializer(),
        responses={
            '200': CartSerializer()
        },

    )
    def delete(self, request):
        try:
            CartModel.objects.get(id=request.data['id'], user=request.user).delete()
            return ResponseSuccess(request=request.method)
        except:
            return ResponseFail(request=request.method)


class OrderView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CartSerializer

    @swagger_auto_schema(
        operation_id='get_order_model',
        operation_description="get_order_model",
        # request_body=OrderShowSerializer(),
        responses={
            '200': OrderShowSerializer()
        },

    )
    def get(self, request):
        orders = OrderModel.objects.filter(user=request.user)
        serializer = OrderShowSerializer(orders, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)

    @swagger_auto_schema(
        operation_id='create_cart_model',
        operation_description="To create cart model",
        # request_body=OrderShowSerializer(),
        responses={
            '200': OrderShowSerializer()
        },

    )
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

    @swagger_auto_schema(
        operation_id='create_order_model',
        operation_description="To change carts to order",
        request_body=PutSerializer(),
        responses={
            '200': OrderShowSerializer()
        },

    )
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

