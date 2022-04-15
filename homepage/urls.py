from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('ledger',views.ledger.as_view(),name='ledger')
]
