.. _docutils: http://docutils.sourceforge.net/
.. _Django: https://www.djangoproject.com/
.. _django-materialize-css: https://pypi.python.org/pypi/django-materialize-css/
.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _Materialize: http://materializecss.com 

Introduction
============

This is a `Django`_ application to add `django-crispy-forms`_ layout objects for `Materialize`_.

This app does not embed a `Materialize`_ release, you will have to install `django-materialize-css`_ as a dependency or download/ link to latests updates of materializecss in your project.

Links
*****

* Read the documentation on `Read the docs soon!`;
* Download and install this from `PyPi package <https://pypi.python.org/pypi/crispy-forms-materialize/>`__
* Clone it on this `Github repository <https://github.com/edvm/crispy-forms-materialize>`__

Requires
========

* `django-crispy-forms`_ above 1.4.x version
* `django-materialize-css`_ above 1.4.x version (optional)

You can get django-materialize-css from `PyPI <https://pypi.python.org/pypi/django-materialize-css/>`__ and `github <https://github.com/edvm/django-materialize-css>`__

Installation
============

Probably the best way to install is by using `PIP`::

    $ pip install crispy-forms-materialize

If you want to stay on the bleeding edge of the app::

    $ git clone https://github.com/edvm/crispy-forms-materialize.git
    $ cd crispy-forms-materialize
    $ python setup.py install


Then add the app in your project's ``INSTALLED_APPS`` like this :

.. sourcecode:: python

    INSTALLED_APPS = (
        ...
        'materialize',
        'crispy_forms',
        'crispy_forms_materialize',
        ...
    )

Then change crispy template pack settings to start using it in your forms:

.. sourcecode:: python

    # Default layout to use with "crispy_forms"
    CRISPY_TEMPLATE_PACK = 'materialize_css_forms'

All other `django-crispy-forms`_ settings option apply, see its documentation for more details.
