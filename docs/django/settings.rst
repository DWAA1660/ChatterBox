==========================
ChatterBox Django Settings
==========================

You can edit the ChatterBox configuration through your Django settings.py file.

.. code-block:: python

   ChatterBox = {
       'name': 'Tech Support Bot',
       'logic_adapters': [
           'chatterbox.logic.MathematicalEvaluation',
           'chatterbox.logic.TimeLogicAdapter',
           'chatterbox.logic.BestMatch'
       ]
   }

Any setting that gets set in the ChatterBox dictionary will be passed to the chat bot that powers your django app.

Additional Django settings
==========================

- ``django_app_name`` [default: 'django_chatterbox'] The Django app name to look up the models from.