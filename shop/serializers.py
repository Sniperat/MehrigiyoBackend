from rest_framework import serializers
from .models import PicturesMedicine, TypeMedicine, Medicine, CartModel, OrderModel, Advertising
from account.serializers import DeliverAddressSerializer
from account.models import DeliveryAddress


class AdvertisingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertising
        fields = '__all__'


class PicturesMedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = PicturesMedicine
        fields = '__all__'


class TypeMedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeMedicine
        fields = '__all__'


class MedicineSerializer(serializers.ModelSerializer):
    pictures = PicturesMedicineSerializer(many=True)
    # is_favorite = serializers.ReadOnlyField(source='is_favorite')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            user = self.context['user']
            if instance in user.favorite_medicine.all():

                representation['is_favorite'] = True
            else:
                representation['is_favorite'] = False
        except:
            print('asdasdasdasd')
        representation['rate'] = instance.total_rate or 0
        return representation

    class Meta:
        model = Medicine
        fields = "__all__"




class CartSerializer(serializers.ModelSerializer):
    product = MedicineSerializer(read_only=True)
    user = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = CartModel
        fields = ('id', 'user', 'amount', 'product', 'get_total_price')
        extra_kwargs = {
            'user': {'required': False},
            'amount': {'required': False},
            'product': {'required': False}
        }

    def create(self, validated_data):
        request = self.context.get('request', None)
        instance = self.Meta.model(**validated_data)
        instance.user = request.user
        # instance.product = request.data['product']
        instance.save()
        return instance


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderModel
        fields = ('id', 'user', 'credit_card', 'shipping_address', 'cart_products', 'price', 'payment_type',
                  'payment_status', 'delivery_status', 'created_at')
        extra_kwargs = {
            'cart_products': {'required': False}
        }


class OrderShowSerializer(serializers.ModelSerializer):
    shipping_address = DeliverAddressSerializer()
    cart_products = CartSerializer(many=True)

    class Meta:
        model = OrderModel
        fields = '__all__'
        extra_kwargs = {
            'delivery': {'required': False}
        }

    def update(self, instance, validated_data):
        try:
            id = validated_data['shipping_address']
            da = DeliveryAddress.objects.get(id=id)
            instance.shipping_address = da
            instance.price = instance.price + da.region.delivery_price
            instance.save()

        except:
            pass
        print(instance)
        print(validated_data)
        instance.save()


class ListSerializer(serializers.Serializer):
    list = serializers.CharField()