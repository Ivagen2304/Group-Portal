from django.urls import path
from .views import PortfolioListView, PortfolioDetail, PortfolioDelete, PortfolioUpdate, PortfolioCreate

urlpatterns = [
    path('', PortfolioListView.as_view(), name = "portfoliolist"),
    path('<int:pk>', PortfolioDetail.as_view(), name = "portfoliodetail"),
    path('delete/<int:pk>', PortfolioDelete.as_view(), name = "portfoliodelete"),
    path('update/<int:pk>', PortfolioUpdate.as_view(), name = "portfolioupdate"),
    path('create/', PortfolioCreate.as_view(), name = "portfoliocreate")
]