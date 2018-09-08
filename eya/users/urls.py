# -*- coding: utf-8 -*-
from django.conf.urls import url
from users.views import RegisterCustomerForm, CustomerDetailView

urlpatterns = [
    url(r'^register/$', RegisterCustomerForm.as_view(), name='register-customer'),
    url(r'^profile/(?P<pk>[0-9]+)/$', CustomerDetailView.as_view(), name='customer-profile'),
]