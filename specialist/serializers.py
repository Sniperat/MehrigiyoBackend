from django.db.models import Sum
from rest_framework import serializers

from account.models import UserModel
from .models import Doctor, TypeDoctor, RateDoctor, Advertising, AdviceTime
from comment.models import CommentDoctor


class AdvertisingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertising
        fields = '__all__'


class TypeDoctorSerializer(serializers.ModelSerializer):
    # get_doctors_count = serializers.SerializerMethodField('')
    class Meta:
        model = TypeDoctor
        fields = ['id', 'name', 'name_uz', 'name_ru', 'name_en', 'image', 'get_doctors_count']


class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField()
    type_doctor = TypeDoctorSerializer()
    rate = serializers.CharField(read_only=True, )
    is_favorite = serializers.BooleanField(read_only=True, )
    top = serializers.BooleanField(read_only=True, )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            user = self.context['user']
            if instance in user.favorite_medicine.all():

                representation['is_favorite'] = True
            else:
                representation['is_favorite'] = False
        except:
            pass
        # doctors = CommentDoctor.objects.filter(doctor=representation,)
        # representation['rate'] = sum(instance.comments_doc.values('rate', flat=True))
        try:
            representation['rate'] = instance.total_rate or 0
            print('asdasd 1')
            print(instance.total_rate)

            if representation['rate'] >= 4.5 and representation['review'] >= 15:
                print('asdasd 2')

                representation['top'] = True
            else:
                print('asdasd 3')

                representation['top'] = False

        except:
            pass
        # representation['rate'] = Sum(instance__comments_doc__rate)
        return representation

    class Meta:
        model = Doctor
        fields = '__all__'
        extra_fields = ['rate', 'is_favorite']


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = RateDoctor
        fields = '__all__'

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.client = self.context['request'].user
        instance.save()
        return instance


class AdvicecDocSerializer(serializers.Serializer):
    start_time = serializers.DateTimeField()
    end_time = serializers.DateTimeField()
    id = serializers.IntegerField()


class AdviceSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()

    class Meta:
        model = AdviceTime
        fields = '__all__'