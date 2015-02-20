=====
django-adminflex
=====

django-adminflex is a simple Django app to provide New Zealand power companies.

Quick start
-----------

1. Add "adminflex" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'adminflex',
    ]

2. Include the URLconf in your project urls.py like this::

    url(r'^adminflex/', include('adminflex.urls')),

3. Run `python manage.py migrate` to create the models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create an object (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/adminflex/

6. Add to requirements.txt::

    -e git+https://bitbucket.org/nodedigital/django-adminflex#egg=adminflex

Usage
--------

    >>> from adminflex.models import Company
    >>> objs = Company.objects.all()
    >>> obj = objs[0]
    >>> obj.name
    u'Contact Energy'
    >>> obj.slug
    u'contact-energy'
    >>> obj.site
    u'https://www.contact.co.nz'
    >>> obj.get_logo()
    u'/static/adminflex/img/contact-energy.jpg'
