from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    path('shop/detail/<int:id>/', shop_detail),
    path('product/detail/<int:id>/', product_detail),
    path('product/list/', ProductListView.as_view()),
]
