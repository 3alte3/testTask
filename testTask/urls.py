from django.contrib import admin
from django.urls import path, include, re_path
from category.views import CreateCategory
from rest_framework import routers
from registration.views import Profile
from transaction.views import TransactionView
from statistic.views import Statistics

router = routers.SimpleRouter()
router.register(r'category', CreateCategory)
router.register(r'user',Profile)
router.register(r'tc',TransactionView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transaction/',include(router.urls)),
    path('ccd/', include(router.urls)),
    path('ccd/category/<str:name>',CreateCategory.as_view({'delete':'destroy'})),
    path('profile/',include(router.urls)),
    path('stat/',Statistics.as_view()),
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
