from rest_framework import routers
from prices.views import ListPlans

price_router = routers.DefaultRouter()
price_router.register(r'plans', ListPlans, 'plans')
