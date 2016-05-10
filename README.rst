.. _docutils: http://docutils.sourceforge.net/
.. _Django: https://www.djangoproject.com/
.. _django-materialize-css: https://pypi.python.org/pypi/django-materialize-css/0.0.1
.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _Materialize: http://materializecss.com 

Introduction
============

This is a `Django`_ application to add `django-crispy-forms`_ layout objects for `Materialize`_.

This app does not embed a `Materialize`_ release, you will have to install `django-materialize-css`_
as a dependency.

Links
*****

* Read the documentation on `Read the docs soon!`;
* Download his `PyPi package https://pypi.python.org/pypi/django-materialize-css/0.0.1`
* Clone it on his `Github repository <https://github.com/edvm/crispy-forms-materialize`;

Requires
========

* `django-crispy-forms`_ = 1.4.x;
* `django-materialize-css`_ = 1.4.x;

Installation
============

Just register the app in your project settings like that :

.. sourcecode:: python

    INSTALLED_APPS = (
        ...
        'materialize',
        'crispy_forms',
        'crispy_forms_materialize',
        ...
    )

Then append this part to specify usage of the Materialize set :

.. sourcecode:: python

    # Default layout to use with "crispy_forms"
    CRISPY_TEMPLATE_PACK = 'materialize_css_forms'

All other `django-crispy-forms`_ settings option apply, see its documentation for more details.
