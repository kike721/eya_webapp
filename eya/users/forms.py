# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from store.models import Cart
from users.email import register_confirm_email
from users.models import Customer, Manager, Seller, UserToken


def validate_fields(cleaned_data, update):
    if 'email' in cleaned_data:
        email = cleaned_data['email']
        if update:
            user = cleaned_data['user']
            if User.objects.filter(email=email).exclude(
                    email=user.email).count() > 0:
                raise forms.ValidationError(
                    'Ya existe un usuario con este correo.')
        else:
            if User.objects.filter(email=email).count() > 0:
                raise forms.ValidationError(
                    'Ya existe un usuario con este correo.')
    else:
        raise forms.ValidationError(
            'El campo de correo es obligatorio.')
    if 'type' in cleaned_data:
        if cleaned_data['type'] == '':
            raise forms.ValidationError(
                'Debes seleccionar un tipo de administrador.')
    else:
        raise forms.ValidationError(
            'Debes seleccionar un tipo de administrador.')
    if 'password' in cleaned_data and 'repeat_password' in cleaned_data:
        password = cleaned_data['password']
        repeat_password = cleaned_data['repeat_password']
        if not update:
            if len(password) == 0 or len(repeat_password) == 0:
                raise forms.ValidationError(
                    'Debes ingresar una contraseña.')
        if password != repeat_password:
            raise forms.ValidationError(
                'Las contraseñas deben ser iguales.')
        else:
            setPassword = False
            if len(password) > 0 and len(repeat_password) > 0:
                setPassword = True
                if len(password) < 8:
                    raise forms.ValidationError(
                        'La contraseña debe contener mínimo 8 caracteres.')
            email = cleaned_data["email"]
            password = cleaned_data["password"]
            if not update:
                user = User.objects.create_user(
                    email, email, password)
            else:
                user = cleaned_data['user']
                
                user.email = email
                user.username = email
                if setPassword:
                    user.set_password(password)
            user.first_name = cleaned_data["name"]
            user.last_name = cleaned_data["last_name"]
            user.is_staff = True
            user.save()
            cleaned_data["user"] = user


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
        if 'password' in data:
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
                user=user, name = data['name'], rfc = data['rfc'],
                street = data['street'], phone = data['phone'],
                state= data['state'], active=data['active'])
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
        if 'password' in data:
            user.set_password(data['password'])
        user.save()
        return customer

    def save_m2m(self):
        return True


class SellerForm(forms.ModelForm):

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
                {'email': instance.user.email,
                 'first_name': instance.user.first_name,
                 'last_name': instance.user.last_name
                 }
            )
        super(SellerForm, self).__init__(*args, **kwargs)

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
                username=data['email'], email=data['email'],
                first_name=data['first_name'], last_name=data['last_name'])
        else:
            user = data['user']
            user.username = data['email']
            user.email = data['email']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
        if 'password' in data:
            user.set_password(data['password'])
        user.save()
        if not self.update:
            seller = Seller.objects.create(user=user)
        else:
            seller = Seller.objects.get(user=user)
        return seller

    def save_m2m(self):
        return True


class ManagerForm(forms.ModelForm):

    email = forms.EmailField(required=True)
    password = forms.CharField(
        label=u"Contraseña", widget=forms.PasswordInput, required=False)
    repeat_password = forms.CharField(
        label=u"Repetir contraseña", widget=forms.PasswordInput,
        required=False)
    name = forms.CharField(label=u"Nombre", required=False)
    last_name = forms.CharField(label=u"Apellidos", required=False)

    class Meta:
        model = Manager
        fields = ('user', 'type')
        widgets = {'user': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        self.update = False
        if not kwargs.get('instance') is None:
            self.update = True
            if 'initial' not in kwargs:
                kwargs['initial'] = {}
                instance = kwargs['instance']
            kwargs['initial'].update(
                {'email': instance.user.email,
                 'name': instance.user.first_name,
                 'last_name': instance.user.last_name,
                 }
            )
        super(ManagerForm, self).__init__(*args, **kwargs)
        self.fields['type'].choices = (
            (Manager.NONE, u'-------'),
            (Manager.SUPERADMIN, u'Super Admin'),
            (Manager.TRADER, u'Cotizador'),
            (Manager.PROVIDER, u'Surtidor'),
            (Manager.BILLING, u'Facturación'),)

    def clean(self):
        cleaned_data = super(ManagerForm, self).clean()
        validate_fields(cleaned_data, self.update)


class ManagerAdminForm(forms.ModelForm):

    email = forms.EmailField(required=True)
    password = forms.CharField(
        label=u"Contraseña", widget=forms.PasswordInput, required=False)
    repeat_password = forms.CharField(
        label=u"Repetir contraseña", widget=forms.PasswordInput,
        required=False)
    name = forms.CharField(label=u"Nombre", required=False)
    last_name = forms.CharField(label=u"Apellidos", required=False)

    class Meta:
        model = Manager
        fields = ('user', 'type')
        widgets = {'user': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        self.update = False
        if not kwargs.get('instance') is None:
            self.update = True
            if 'initial' not in kwargs:
                kwargs['initial'] = {}
                instance = kwargs['instance']
            kwargs['initial'].update(
                {'email': instance.user.email,
                 'name': instance.user.first_name,
                 'last_name': instance.user.last_name,
                 }
            )
        super(ManagerAdminForm, self).__init__(*args, **kwargs)
        self.fields['type'].choices = (
            (Manager.NONE, u'-------'),
            (Manager.SUPERADMIN, u'Super Admin'),
            (Manager.TRADER, u'Cotizador'),
            (Manager.PROVIDER, u'Surtidor'),
            (Manager.BILLING, u'Facturación'),
        )

    def clean(self):
        cleaned_data = super(ManagerAdminForm, self).clean()
        validate_fields(cleaned_data, self.update)