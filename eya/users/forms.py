# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from store.models import Cart
from users.email import register_confirm_email
from users.models import Customer, Seller, UserToken


class CustomerForm(forms.ModelForm):

    email = forms.CharField(
        label='Email', max_length=255, widget=forms.EmailInput)
    password = forms.CharField(
        label=u'Contraseña', max_length=255,
        widget=forms.PasswordInput(), required=False)
    confirm_password = forms.CharField(
        label=u'Confirmar contraseña', max_length=255,
        widget=forms.PasswordInput(), required=False)

    class Meta:
        model = Customer
        fields = ('name', 'rfc', 'street', 'state', 'phone')
        # widgets = {'user': forms.HiddenInput(attrs={'required':False})}

    def __init__(self, *args, **kwargs):
        self.update = False
        if not kwargs.get('instance') is None:
            self.update = True
            if 'initial' not in kwargs:
                kwargs['initial'] = {}
                instance = kwargs['instance']
            kwargs['initial'].update(
                {'email': instance.user.email}
            )
        super(CustomerForm, self).__init__(*args, **kwargs)

    def clean(self):
        data = self.cleaned_data
        password = ''
        confirm_password = ''
        if 'password' in data:
            password = data['password']
        if 'confirm_password' in data:
            confirm_password = data['confirm_password']
        if (len(password) == 0 or len(confirm_password) == 0) and not self.update:
            raise forms.ValidationError(
                'Debes ingresar una contraseña.')
        if password != '' and confirm_password != '':
            if password != confirm_password:
                raise forms.ValidationError(u"Las contraseñas deben ser iguales")
        if 'email' in data:
            email = data['email']
            if self.update:
                user = self.instance.user
                if User.objects.filter(username=email).exclude(
                        username=user.username).count() > 0:
                    raise forms.ValidationError(
                        'Ya existe un usuario con este correo.')
            else:
                if User.objects.filter(username=email).count() > 0:
                    raise forms.ValidationError(
                        'Ya existe un usuario con este correo.')
        return data

    def save(self, commit=True):
        data = self.cleaned_data
        if not self.update:
            user = User.objects.create(
                username=data['email'], email=data['email'], is_active=False)
            customer = Customer.objects.create(
                user=user, name=data['name'], rfc=data['rfc'],
                street=data['street'], phone=data['phone'], state=data['state'])
            token = get_random_string(length=64)
            user_token = UserToken.objects.create(
                email=data['email'],
                token=token,
                is_reset=False
            )
            # Send email to user
            register_confirm_email(token, customer)
        else:
            user = self.instance.user
            user.username = data['email']
            user.email = data['email']
            customer = self.instance
            customer.name = data['name']
            customer.rfc = data['rfc']
            customer.street = data['street']
            customer.state = data['state']
            customer.phone = data['phone']
            customer.save()
        if 'password' in data and data['password'] != '':
            user.set_password(data['password'])
        user.save()
        return customer

    def save_m2m(self):
        return True


class CustomerAdminForm(forms.ModelForm):

    email = forms.CharField(
        label='Email', max_length=255, widget=forms.EmailInput)
    password = forms.CharField(
        label=u'Contraseña', max_length=255,
        widget=forms.PasswordInput(), required=False)
    confirm_password = forms.CharField(
        label=u'Confirmar contraseña', max_length=255,
        widget=forms.PasswordInput(), required=False)

    class Meta:
        model = Customer
        fields = ('name', 'rfc', 'street', 'state', 'phone', 'active')

    def __init__(self, *args, **kwargs):
        self.update = False
        if not kwargs.get('instance') is None:
            self.update = True
            if 'initial' not in kwargs:
                kwargs['initial'] = {}
                instance = kwargs['instance']
            kwargs['initial'].update(
                {'email': instance.user.email}
            )
        super(CustomerAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        data = self.cleaned_data
        password = ''
        confirm_password = ''
        if 'password' in data:
            password = data['password']
        if 'confirm_password' in data:
            confirm_password = data['confirm_password']
        if (len(password) == 0 or len(confirm_password) == 0) and not self.update:
            raise forms.ValidationError(
                'Debes ingresar una contraseña.')
        if password != '' and confirm_password != '':
            if password != confirm_password:
                raise forms.ValidationError(u"Las contraseñas deben ser iguales")
        if 'email' in data:
            email = data['email']
            if self.update:
                user = self.instance.user
                if User.objects.filter(username=email).exclude(
                        username=user.username).count() > 0:
                    raise forms.ValidationError(
                        'Ya existe un usuario con este correo.')
            else:
                if User.objects.filter(username=email).count() > 0:
                    raise forms.ValidationError(
                        'Ya existe un usuario con este correo.')
        return data

    def save(self, commit=True):
        data = self.cleaned_data
        if not self.update:
            user = User.objects.create(
                username=data['email'], email=data['email'], is_active=data['active'])
            customer = Customer.objects.create(
                user=user, name=data['name'], rfc=data['rfc'],
                street=data['street'], phone=data['phone'],
                state=data['state'], active=data['active'])
            Cart.objects.create(customer=customer)
        else:
            user = self.instance.user
            user.username = data['email']
            user.email = data['email']
            user.is_active = data['active']
            customer = self.instance
            customer.name = data['name']
            customer.rfc = data['rfc']
            customer.street = data['street']
            customer.state = data['state']
            customer.phone = data['phone']
            customer.active = data['active']
            customer.save()
        if 'password' in data and data['password'] != '':
            user.set_password(data['password'])
        user.save()
        return customer

    def save_m2m(self):
        return True


class SellerAdminForm(forms.ModelForm):

    email = forms.CharField(
        label='Email', max_length=255, widget=forms.EmailInput)
    password = forms.CharField(
        label=u'Contraseña', max_length=255,
        widget=forms.PasswordInput(), required=False)
    confirm_password = forms.CharField(
        label=u'Confirmar contraseña', max_length=255,
        widget=forms.PasswordInput(), required=False)

    class Meta:
        model = Seller
        fields = ('user', 'name', 'rfc', 'address', 'phone')
        widgets = {'user': forms.HiddenInput(attrs={'required':False})}

    def __init__(self, *args, **kwargs):
        self.update = False
        if not kwargs.get('instance') is None:
            self.update = True
            if 'initial' not in kwargs:
                kwargs['initial'] = {}
                instance = kwargs['instance']
            kwargs['initial'].update(
                {'email': instance.user.email}
            )
        super(SellerAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        data = self.cleaned_data
        password = ''
        confirm_password = ''
        if 'password' in data:
            password = data['password']
        if 'confirm_password' in data:
            confirm_password = data['confirm_password']
        if (len(password) == 0 or len(confirm_password) == 0) and not self.update:
            raise forms.ValidationError(
                'Debes ingresar una contraseña.')
        if password != '' and confirm_password != '':
            if password != confirm_password:
                raise forms.ValidationError(u"Las contraseñas deben ser iguales")
        if 'email' in data:
            email = data['email']
            if self.update:
                user = data['user']
                if User.objects.filter(username=email).exclude(
                        username=user.username).count() > 0:
                    raise forms.ValidationError(
                        'Ya existe un usuario con este correo.')
            else:
                if User.objects.filter(username=email).count() > 0:
                    raise forms.ValidationError(
                        'Ya existe un usuario con este correo.')
            return data

    def save(self, commit=True):
        data = self.cleaned_data
        if not self.update:
            user = User.objects.create(
                username=data['email'], email=data['email'], is_active=True)
            seller = Seller.objects.create(
                user=user, name=data['name'], rfc=data['rfc'],
                address=data['address'], phone=data['phone'])
        else:
            user = self.instance.user
            user = data['user']
            user.username = data['email']
            user.email = data['email']
            seller = self.instance
            seller.name = data['name']
            seller.rfc = data['rfc']
            seller.address = data['address']
            seller.phone = data['phone']
        if 'password' in data and data['password'] != '':
            user.set_password(data['password'])
        user.save()
        seller.save()
        return seller

    def save_m2m(self):
        return True
