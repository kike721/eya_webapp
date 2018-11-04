# -*- coding: utf-8 -*-
from django.conf.urls import url
from users.views import (
    RegisterCustomerForm, CustomerDetailView, CustomerRequestRegister, SellerDetailView,
    user_confirm, set_customer)

urlpatterns = [
    url(r'^registro/$', RegisterCustomerForm.as_view(),
        name='register-customer'),
    url(r'^perfil/(?P<pk>[0-9]+)/$', CustomerDetailView.as_view(),
        name='customer-profile'),
    url(r'^registro/notificacion/$', CustomerRequestRegister.as_view(),
        name='customer-request-register'),
    url(r'^vendedor/(?P<pk>[0-9]+)/$', SellerDetailView.as_view(),
        name='seller-profile'),
    url(r'confirmacion/(?P<token>\w+)/$', user_confirm, name='customer-confirm'),
    url(r'customer/selected/$', set_customer, name='customer-selected'),
]