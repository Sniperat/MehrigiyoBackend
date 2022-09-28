from rest_framework import serializers
from .models import UserModel, CountyModel, RegionModel, DeliveryAddress, OfferModel
from config.validators import PhoneValidator


class OfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = OfferModel
        fields = '__all__'


class PkSerializer(serializers.Serializer):
    pk = serializers.IntegerField(required=True)


class RegionPostSerializer(serializers.Serializer):
    region = serializers.IntegerField(required=True)


class SmsSerializer(serializers.Serializer):
    phone = serializers.CharField(validators=[PhoneValidator()])


class ConfirmSmsSerializer(serializers.Serializer):
    phone = serializers.CharField(validators=[PhoneValidator()])
    code = serializers.CharField(min_length=6, max_length=6)


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 'avatar']
        extra_kwargs = {
            'password': {'write_only': True},
            'avatar': {'required': False},
            'email': {'required': False}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CountyModel
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    # country = CountrySerializer()
    id = serializers.ReadOnlyField()

    class Meta:
        model = RegionModel
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    address = RegionSerializer(read_only=True)

    class Meta:
        model = UserModel
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'avatar', 'address', 'language',
                  'favorite_medicine', 'favorite_doctor', 'theme_mode']
        extra_kwargs = {
            'username': {'read_only': True},
            'favorite_medicine': {'read_only': True},
            'favorite_doctor': {'read_only': True},
            'address': {'read_only': True},
            'first_name': {'required': False},
            'last_name': {'required': False},
            'email': {'required': False},
            'avatar': {'required': False},
            'language': {'required': False},
            'theme_mode': {'required': False},
        }


class DeliverAddressSerializer(serializers.ModelSerializer):
    region = RegionSerializer()

    class Meta:
        model = DeliveryAddress
        fields = ['id', 'name', 'region', 'full_address', 'apartment_office', 'floor', 'door_or_phone', 'instructions']
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'required': False},
            'region': {'required': False},
            'full_address': {'required': False},
            'apartment_office': {'required': False},
            'floor': {'required': False},
            'door_or_phone': {'required': False},
            'instructions': {'required': False},
        }


