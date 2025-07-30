from rest_framework import serializers

from ..models import WeigthHistory


class WeigthHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = WeigthHistory
        fields = ["id", "weigth", "imc_on_date", "created_at"]
        read_only_fields = fields
