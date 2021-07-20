
from django.urls.conf import include
from onlineshop.api.views import BrandViewSet, CategoryViewSet, ProductViewSet
from onlineshop.models import Brand, Category, Product
from django.urls import path
from rest_framework import routers


router = routers.DefaultRouter()
router.register('brands', BrandViewSet)
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)



urlpatterns = [
    path('v1/', include(router.urls)),
    # path('v1/branches/', BranchListView.as_view(), name = 'branches'),
    # path('v1/branches/<int:pk>/', BranchDetailView.as_view(), name='branch_detail'),
    # path('v1/groups/', GroupListView.as_view(), name = 'groups'),
    # path('v1/groups/<int:pk>/', GroupDetailView.as_view(), name='group_detail'),
    # path('v1/students/', StudentListView.as_view(), name = 'students'),
    # path('v1/students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
]