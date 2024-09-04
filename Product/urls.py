from django.urls import path,include
from rest_framework import routers
from .views import ProductView,CategoryView,BrandView

router = routers.DefaultRouter()
router.register(r'product_category',CategoryView)
router.register(r'product_brand',BrandView)
urlpatterns = [
    path('get_all/',ProductView.as_view({'get':'list'})),
    path('add_product/<userId>/',ProductView.as_view({'post':'create'})),
    path('update_product/<id>/',ProductView.as_view({'update':'patch'})),
    path('delete_product/<id>/',ProductView.as_view({'delete':'destroy'})),


    path('',include(router.urls)),
    # path('',include(router.urls))
]
