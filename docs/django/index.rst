==================
Django Integration
==================

ChatterBox has direct support for integration with Django's ORM.
It is relatively easy to use ChatterBox within your Django application
to create conversational pages and endpoints.

.. toctree::
   :maxdepth: 2

   settings
   views
   wsgi

Install packages
================

Begin by making sure that you have installed both ``django`` and ``chatterbox``.

.. sourcecode:: sh

   pip install django chatterbox

For more details on installing Django, see the `Django documentation`_.

Installed Apps
--------------

Add ``chatterbox.ext.django_chatterbox`` to your ``INSTALLED_APPS`` in the
``settings.py`` file of your Django project.

.. code-block:: python

   INSTALLED_APPS = (
       # ...
       'chatterbox.ext.django_chatterbox',
   )


Migrations
----------

You can run the Django database migrations for your chat bot with the
following command.

.. sourcecode:: sh

   python manage.py migrate django_chatterbox

MongoDB and Django
------------------

ChatterBox has a storage adapter for MongoDB but it does not work with Django.
If you want to use MongoDB as your database for Django and your chat bot then
you will need to install a **Django storage backend** such as `Django MongoDB Engine`_.

The reason this is required is because Django's storage backends are different
and completely separate from ChatterBox's storage adapters.

.. _Django documentation: https://docs.djangoproject.com/en/dev/intro/install/
.. _Django MongoDB Engine: https://django-mongodb-engine.readthedocs.io/
