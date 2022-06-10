from django.contrib import admin
from django.urls import path, include
from .views import AnketaFromBitrix

urlpatterns = [
    path('', AnketaFromBitrix.indexPage, name="index"),
    path('deal/<int:idFromBitrix>', AnketaFromBitrix.dealPage, name="dealAnketa"),
    path('lead/<int:idFromBitrix>', AnketaFromBitrix.leadPage, name="leadAnketa"),
]
