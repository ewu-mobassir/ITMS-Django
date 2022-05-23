"""ITMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from account.views import user_register_view, login_view, logout_view, agency_register_view
from spots.views import add_spot_view, browse_spot_view, add_spot_image, add_review, view_review, set_geoPosition, add_hotel_view, \
    add_offer_view, book_tour_view, spot_offers_view
from userprofile.views import profile_view, edit_profile_view

urlpatterns = [
    path('', include('home.urls'), name='home'),
    path('admin/', admin.site.urls, name='django_admin'),
    path('register/',user_register_view, name='user_reg'),
    path('agencyregister/',agency_register_view, name='agency_reg'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('addspot/', add_spot_view, name='add_spot'),
    path('browsespot/', browse_spot_view, name='browse_spot'),
    path('addimage/<str:pk>', add_spot_image, name='add_image'),
    path('addreview/<str:pk>', add_review, name='add_review'),
    path('profile/',profile_view, name='view_profile'),
    path('spotreview/<str:pk>',view_review, name='view_review'),
    path('setSpotGeo/<str:pk>',set_geoPosition, name='set_spot_geo'),
    path('editprofile/',edit_profile_view, name='edit_profile'),
    path('addhotel/', add_hotel_view, name='add_hotel'),
    path('createoffer/', add_offer_view, name='create_offer'),
    path('booking/<str:pk>', book_tour_view, name='booking'),
    path('browseoffers/<str:pk>', spot_offers_view, name='browse_offers'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

