from .api_views import (CreateDashboardProfile,
                        UpdateDashboardProfile,
                        DestroyProfile,
                        RetrieveProfile,
                        DashboardProfileTokenObtainPairView,
                        DashboardProfileTokenRefreshView,
                        CheckProfile)
from .weigth_history_viewset import WeigthHistoryViewSet


__all=[
    CreateDashboardProfile,
    UpdateDashboardProfile,
    DestroyProfile,
    RetrieveProfile,
    DashboardProfileTokenObtainPairView,
    DashboardProfileTokenRefreshView,
    CheckProfile,
    WeigthHistoryViewSet
]