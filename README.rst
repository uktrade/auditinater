Auditinater
===========

.. contents::

Hunt for PaaS password based login's and report them on the SRE slack channel.
With a few exceptions, only google SSO accounts should be allowed. Google is
used as the central identity management system.


Development
-----------

I'm using make, docker-compose, python3 and virtualenvwrappers to develop the
project locally. I currently work of Mac OSX for development and use Homebrew
to install what I need. Your mileage may vary. To set up the code for development
you can do::

   mkvirtualenv --clear -p python3 audit
   make test_install

   # Once-off per new audit env setup:
   python -m pip install --upgrade pip pip-tools

   # To update all dependancies when your ready to. This will update the
   # pinned version numbers in requirments.txt.
   pip-compile requirements.in

There is a ``make install``. This only installs the apps dependancies and not
those needed for testing. To run the service locally in the dev environment do::

   # activate the env
   workon audit

   # run dependant services via docker compose (in its own terminal)
   make up

   # run the periodic task manager (in its own terminal)
   make runbeat

   # run the webapp (in its own terminal)
   make runserver

Using the Makefile to run the webapp/worker/beat is only meant for local
development. It is not for live environment use (staging/production/...)


Testing
~~~~~~~

You can run the tests as follows::

   # activate the env
   workon audit

   # run dependant services via docker compose (in its own terminal)
   make up

   # Run all tests and output a coverage report
   make test
