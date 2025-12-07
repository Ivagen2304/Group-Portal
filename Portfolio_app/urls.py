from django.urls import path
from .views import (
    PortfolioListView,
    PortfolioDetail,
    PortfolioCreate,
    PortfolioUpdate,
    PortfolioDelete,
)

urlpatterns = [
    path("", PortfolioListView.as_view(), name="portfoliolist"),
    path("<int:pk>/", PortfolioDetail.as_view(), name="portfoliodetail"),
    path("create/", PortfolioCreate.as_view(), name="portfoliocreate"),
    path("update/<int:pk>/", PortfolioUpdate.as_view(), name="portfolioupdate"),
    path("delete/<int:pk>/", PortfolioDelete.as_view(), name="portfoliodelete"),
]
