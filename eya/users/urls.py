# -*- coding: utf-8 -*-
from django.conf.urls import url
from users.views import (
    RegisterCustomerForm, CustomerDetailView, CustomerRequestRegister)

urlpatterns = [
    url(r'^registro/$', RegisterCustomerForm.as_view(),
        name='register-customer'),
    url(r'^perfil/(?P<pk>[0-9]+)/$', CustomerDetailView.as_view(),
        name='customer-profile'),
    url(r'^registro/notificacion/$', CustomerRequestRegister.as_view(),
        name='customer-request-register'),
]