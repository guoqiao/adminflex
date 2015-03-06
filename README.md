=====
django-adminflex
=====

django-adminflex is a simple Django app to make django admin responsive.

Core files:

* adminflex.css: override admin css only when necessary.
* admin/base.html: add adminflex.css and a few meta to base.html

Quick start
-----------

1. Install and add to requiremets.txt:

    pip install git+https://github.com/guoqiao/adminflex.git

2. Add "adminflex" to INSTALLED_APPS before django admin:

    INSTALLED_APPS = (
        'adminflex',
        'django.contrib.admin',
        ...
    )

3. Done.


