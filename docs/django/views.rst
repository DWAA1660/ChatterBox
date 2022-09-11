=======================
ChatterBox Django Views
=======================

Example API Views
=================

ChatterBox's Django example comes with an API view that demonstrates
one way to use ChatterBox to create an conversational API endpoint
for your application.

The endpoint expects a JSON request in the following format:

.. code-block:: json

   {"text": "My input statement"}


.. literalinclude:: ../../examples/django_app/example_app/views.py
   :language: python
   :pyobject: ChatterBoxApiView


.. note::

   Looking for the full example? Check it out on GitHub:
   https://github.com/gunthercox/ChatterBox/tree/master/examples/django_app
