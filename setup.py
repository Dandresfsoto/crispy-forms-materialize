from setuptools import setup, find_packages

setup(
    name='crispy-forms-materialize',
    version=__import__('crispy_forms_materialize').__version__,
    description=__import__('crispy_forms_materialize').__doc__,
    long_description=open('README.rst').read(),
    author='Emiliano Dalla Verde Marcozzi',
    author_email='edvm@fedoraproject.org',
    url='http://pypi.python.org/pypi/crispy-forms-materialize',
    license='GPL v3',
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'django-crispy-forms >= 1.4'
    ],
    include_package_data=True,
    zip_safe=False
)
