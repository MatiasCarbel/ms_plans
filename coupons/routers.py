from rest_framework import routers
from .views import ListCoupons 

coupon_router = routers.DefaultRouter()
coupon_router.register(r'coupons', ListCoupons, 'coupons')
