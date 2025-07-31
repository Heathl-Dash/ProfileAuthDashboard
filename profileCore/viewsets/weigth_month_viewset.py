from rest_framework import filters, viewsets

from ..models import MonthWeigth
from ..serializers import WeigthMonthSerializer
from rest_framework.exceptions import PermissionDenied


class WeigthMonthViewSet(viewsets.ModelViewSet):
    queryset = MonthWeigth.objects.all()
    serializer_class = WeigthMonthSerializer
    http_method_names = ["get"]
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        profile = self.request.user
        return MonthWeigth.objects.filter(profile=profile)

    def get_object(self):
        obj = super().get_object()
        if obj.profile != self.request.user:
            raise PermissionDenied("Você não tem permissão para editar essa tarefa!")
        return obj
