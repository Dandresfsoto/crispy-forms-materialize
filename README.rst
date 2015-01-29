.. _docutils: http://docutils.sourceforge.net/
.. _Django: https://www.djangoproject.com/
.. _django-crispy-forms: https://github.com/maraujop/django-crispy-forms
.. _Materialize: http://materializecss.com 

Introduction
============

This is a `Django`_ application to add `django-crispy-forms`_ layout objects for `Materialize`_.

This app does not embed a `Foundation`_ release, you will have to install it yourself.

Links
*****

* Read the documentation on `Read the docs soon!`_;
* Download his `PyPi package <http://pypi.python.org/pypi/crispy-forms-materialize`_;
* Clone it on his `Github repository <https://github.com/edvm/crispy-forms-materialize`_;

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
