from rest_framework import serializers

from ..models import MonthWeigth


class WeigthMonthSerializer(serializers.ModelSerializer):

    class Meta:
        model = MonthWeigth
        fields = ["id", "weigth", "imc_on_date", "created_at"]
        read_only_fields = fields