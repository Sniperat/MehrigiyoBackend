from rest_framework import serializers
from account.models import UserModel, SmsCode, SmsAttempt, CountyModel, RegionModel, DeliveryAddress


class UserModelAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'


class SmsCodeAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsCode
        fields = '__all__'


class SmsAttemptAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsAttempt
        fields = '__all__'


class CountryModelAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountyModel
        fields = '__all__'


class RegionModelAdminSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = RegionModel
        fields = '__all__'


class DeliveryAddressAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAddress
        fields = '__all__'


from chat.models import Message, ChatRoom


class MessageAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class ChatRoomAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'


from comment.models import CommentDoctor, CommentMedicine


class CommentDoctorAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentDoctor
        fields = '__all__'


class CommentMedicineAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentMedicine
        fields = '__all__'


from news.models import NewsModel


class NewsModelAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = '__all__'


from paymeuz.models import PaymeTransactionModel, Card


class PaymeTransactionModelAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymeTransactionModel
        fields = '__all__'


class CardAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'


from shop.models import PicturesMedicine, TypeMedicine, Medicine, CartModel, DeliveryMan, OrderModel


class PicturesMedicineAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = PicturesMedicine
        fields = '__all__'


class TypeMedicineAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeMedicine
        fields = '__all__'


class MedicineAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'


class CartModelAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModel
        fields = '__all__'


class DeliveryManAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryMan
        fields = '__all__'


class OrderModelAdminSerializer(serializers.ModelSerializer):
    user = UserModelAdminSerializer()

    class Meta:
        model = OrderModel
        fields = '__all__'


from specialist.models import TypeDoctor, Doctor, RateDoctor, AdviceTime


class TypeDoctorAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeDoctor
        fields = '__all__'


class DoctorAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class RateDoctorAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateDoctor
        fields = '__all__'


class AdviceTimeAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdviceTime
        fields = '__all__'
