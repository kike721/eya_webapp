# eya_webapp

Webapp Django para Ensambles y Adornos

## Getting Started

Proyecto Django para dar de alta productos y que los clientes puedan realizar pedidos.

### Prerequisites

python 2.7
virtualenv

```
Give examples
```

### Installing

Crear y activar virtualenv

```
virtualenv eya_webapp
source eya_webapp/bin/active
```
Instalar dependencias

```
pip install -r eya_webapp/requirements/requirements.txt
```
Configurar tu base de datos en el archivo eya_webapp/eya/eya/settings.py

Correr migraciones

```
cd eya_webapp/eya/
python manage.py migrate
```

Correr proyecto 

```
python manage.py runserver 8000
```

End with an example of getting some data out of the system or using it for a little demo

## Deployment


## Built With

* [Django](https://www.djangoproject.com/)

## Contributing

* **Valeria Perez** - *Frontend developer* - [ValeriaPerez](https://github.com/ValeriaPerez)
* **Enrique Durán** - *Backend developer* - [kike721](https://github.com/kike721)
