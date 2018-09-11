# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView

from users.models import Customer
from users.forms import CustomerForm

# Create your views here.
class RegisterCustomerForm(CreateView):

	model = Customer
	form_class = CustomerForm
	template_name = 'customer_form.html'


class CustomerDetailView(DetailView):

	model = Customer
	template_name = 'customer_detail.html'


class CustomerRequestRegister(TemplateView):

	template_name = 'request_register.html'
