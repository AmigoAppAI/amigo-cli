Getting Started
===============

Installation
------------

It is recommended you install this package in a virtualenv.

.. code-block:: bash

  # Python 3.10 or higher is required
  python3 -m venv .venv
  source .venv/bin/activate

Install the package from PyPI:

.. code-block:: bash

  python -m pip install amigo

From github:

.. code-block:: bash

  python -m pip install git+https://github.com/AmigoAppAI/amigo-cli.git

Or via brew:

.. code-block:: bash

  brew install amigo

Extras
~~~~~~

If you want to use the whisper transcription on an OS besides macOS or Windows you will need to install PortAudio. For instance, on Ubuntu:

.. code-block:: bash

  sudo apt-get install libportaudio2

In order to use auto context you will need to install ctags:

Windows:

.. code-block:: bash

  choco install universal-ctags

macOS:

.. code-block:: bash

  brew install universal-ctags

Ubuntu:

.. code-block:: bash

  sudo apt install universal-ctags

Basic Usage
-----------

Start amigo with a list of files you want amigo to be able to read and edit and ask for what you want:

.. code-block:: bash

  amigo file1 file2 file3

You can add and remove files from context in a session with the :code:`/include` and :code:`/exclude` commands. For more on context see :ref:`context`. For a list of all commands see :ref:`commands` or enter :code:`/help` in a amigo session.
