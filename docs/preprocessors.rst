=============
Preprocessors
=============

ChatterBox's :term:`preprocessors` are simple functions that modify the input statement
that a chat bot receives before the statement gets processed by the logic adaper.

Here is an example of how to set preprocessors. The ``preprocessors``
parameter should be a list of strings of the import paths to your preprocessors.

.. code-block:: python

   chatbot = ChatBot(
       'Bob the Bot',
       preprocessors=[
           'chatterbox.preprocessors.clean_whitespace'
       ]
   )

Preprocessor functions
======================

ChatterBox comes with several built-in preprocessors.

.. autofunction:: chatterbox.preprocessors.clean_whitespace

.. autofunction:: chatterbox.preprocessors.unescape_html

.. autofunction:: chatterbox.preprocessors.convert_to_ascii


Creating new preprocessors
==========================

It is simple to create your own preprocessors. A preprocessor is just a function
with a few requirements.

1. It must take one parameter, a ``Statement`` instance.
2. It must return a statement instance.
