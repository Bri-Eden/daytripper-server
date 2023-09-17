"""
URL configuration for daytripper project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from daytripperapi.views import register_user, login_user
from rest_framework import routers
from daytripperapi.views import PackListView, PlannerView, ActivityTypeView, ActivityView, ItemTypeView, PackItemView, TransportaionTypeView, TripView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'planner', PlannerView, 'planner')
router.register(r'packlists', PackListView, 'packlist')
router.register(r'activitytypes', ActivityTypeView, 'activitytype')
router.register(r'activities', ActivityView, 'activity')
router.register(r'trips', TripView, 'trips')
router.register(r'itemtypes', ItemTypeView, 'itemtype')
router.register(r'packitems', PackItemView, 'packitem')
router.register(r'transportation', TransportaionTypeView, 'transportation')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
]
