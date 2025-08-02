from rest_framework import filters, viewsets

from ..models import WeigthHistory
from ..serializers import WeigthHistorySerializer
from rest_framework.exceptions import PermissionDenied


class WeigthHistoryViewSet(viewsets.ModelViewSet):
    queryset = WeigthHistory.objects.all()
    serializer_class = WeigthHistorySerializer
    http_method_names = ["get"]
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        profile = self.request.user
        return WeigthHistory.objects.filter(profile=profile)

    def get_object(self):
        obj = super().get_object()
        if obj.profile != self.request.user:
            raise PermissionDenied("Você não tem permissão para editar essa tarefa!")
        return obj
