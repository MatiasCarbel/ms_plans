from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from coupons.models import Coupon
from coupons.serializers import CouponSerializer

# Create your views here.

class ListCoupons(viewsets.ViewSet):
    
    def list(self, request):
        coupon_code = request.query_params.get('code')
        queryset = Coupon.objects.all()

        if coupon_code:
            queryset = Coupon.objects.filter(code = coupon_code)

        
        serializer = CouponSerializer(queryset, many=True)
        return Response(serializer.data)


