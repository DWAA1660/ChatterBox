=======
Filters
=======

Filters are an efficient way to create queries that can be passed to ChatterBox's storage adapters.
Filters will reduce the number of statements that a chat bot has to process when it is selecting a response.

Setting filters
===============

.. code-block:: python

   chatbot = ChatBot(
       "My ChatterBox",
       filters=[filters.get_recent_repeated_responses]
   )

.. automodule:: chatterbox.filters
   :members:
