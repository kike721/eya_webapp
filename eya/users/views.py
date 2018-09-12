# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView

from store.models import Cart
from users.models import Customer, UserToken
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

	template_name = 'register_done.html'


def user_confirm(request, token):
    try:
        user_token = UserToken.objects.get(token=token)
    except UserToken.DoesNotExist:
        return render(request, 'registration/confirm_email.html', {
            'message': "El link de confirmación no es válido."
        })
    except Exception as e:
        # Unknown error
        print 'Getting sign up token. {}'.format(e)

    # Check if token hasn't expired
    if user_token.has_expired():
        user_token.delete()
        return render(request, 'registration/confirm_email.html', {
            'message': "El link de confirmación ha expirado."
        })

    # Get user
    try:
        user = User.objects.get(username=user_token.email)
    except User.DoesNotExist:
        return render(request, 'registration/confirm_email.html', {
            'message': "El link de confirmación no es válido."
        })
    except Exception as e:
        # Unknown error
        print 'Getting user. {}'.format(e)

    user.is_active = True
    user.customer.active = True
    user.save()
    user.customer.save()
    user_token.delete()
    Cart.objects.create(customer=user.customer)
    login(request, user)
    return render(request, 'registration/confirm_email.html', {
        'message': "La cuenta fue activada."
    })