from rest_framework import serializers
from .models import Card

from paymeuz.keywords import METHOD_PERFORM_TRANSACTION, METHOD_CREATE_TRANSACTION, METHOD_CHECK_PERFORM_TRANSACTION, \
    METHOD_CHECK_TRANSACTION, METHOD_CANCEL_TRANSACTION

METHOD_CHOICES = (
    (METHOD_CHECK_PERFORM_TRANSACTION, METHOD_CHECK_PERFORM_TRANSACTION),
    (METHOD_CREATE_TRANSACTION, METHOD_CREATE_TRANSACTION),
    (METHOD_CHECK_TRANSACTION, METHOD_CHECK_TRANSACTION),
    (METHOD_PERFORM_TRANSACTION, METHOD_PERFORM_TRANSACTION),
    (METHOD_CANCEL_TRANSACTION, METHOD_CANCEL_TRANSACTION)
)


class PaycomOperationSerialzer(serializers.Serializer):
    id = serializers.IntegerField()
    method = serializers.ChoiceField(choices=METHOD_CHOICES)
    params = serializers.JSONField()


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = '__all__'
        extra_kwargs = {
            'owner': {'write_only': True, 'required': False},
            'token': {'write_only': True},
            'recurrent': {'write_only': True},
        }

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.owner = self.context['request'].user
        instance.save()
        return instance


class CardInputSerializer(serializers.Serializer):
    number = serializers.CharField(max_length=16)
    expire = serializers.CharField(max_length=4)
