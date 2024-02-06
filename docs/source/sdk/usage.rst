Python SDK Usage
================

The Python SDK allows you to use amigo in your python programs. If you have amigo installed you can use it like this:

.. code-block:: python

   from amigo import Amigo
   client = Amigo(paths=['README.md'])

   client.startup()
   client.call_amigo_auto_accept("Please fix the typos in the Readme.")
   client.shutdown()

All the same options are available as in the command line interface. You can use commands and change configuration by passing in a amigo.Config object.
