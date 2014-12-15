======================
Chapter 1: Hello world
======================

The objective of this chapter is to create a web server that listens
on a TCP port and responds with "Hello, world!" when the server root
(i.e. the path "/") is requested.

Pure Python
-----------

First, let's see how we can do it with pure :ref:`Python <fpp>` before
going on to do it with Django.

.. literalinclude:: examples/chapter_01/hello_pure_python.py

If you execute this program and visit http://localhost:8000/ with your
browser, you should see it in action.

Installing Django and creating a project and app
------------------------------------------------

Doing the same thing with Django is considerably more complicated (but
it scales; whereas if we added functionality to the pure python
version it would become chaotic very soon).

First, make sure you have Django installed. Assuming you are using
:ref:`virtualenv <fpp>`, a simple ``pip install django`` should
suffice.

Next, we need to create a Django project and a Django app:

.. code-block:: sh

    django-admin startproject my_first_django_project
    cd my_first_django_project
    python manage.py startapp hello

We now have a project named ``my_first_django_project`` and an app
named ``hello``. The concept of a Django app is a big discussion which
we will leave for later. For now we can make the simplifying
assumption that a project consists of one or more apps.

When we executed ``python manage.py startapp hello``, Django created
a directory :file:`hello` with several files. In this first chapter we
will not be using some of these files, so it's better to get them out
of the way. Delete the files ``hello/admin.py`` and
``hello/models.py``, and the directory ``hello/migrations``.

Writing the code
----------------

First, edit :file:`hello/views.py` so that it contains this:

.. literalinclude:: examples/chapter_01/my_first_django_project/hello/views.py

If you've met the term "view" in the past, beware: Django's usage of
the term might be completely different from what you've seen. Some
texts use the term "controller" or "logic" or "functionality" instead,
and they use "view" or "presentation" or "appearance" for what Django
calls a template.  In Django parlance, a view is a Python class (or a
Python function, but this is legacy).

Next, create :file:`hello/urls.py` with the following contents:

.. literalinclude:: examples/chapter_01/my_first_django_project/hello/urls.py

Change :file:`my_first_django_project/urls.py` so that it looks like
this:

.. literalinclude:: examples/chapter_01/my_first_django_project/my_first_django_project/urls.py

Finally, edit :file:`my_first_django_project/settings.py`. Around line
55 the ``DATABASES`` variable is defined; remove the definition.
Around line 30 a variable called ``INSTALLED_APPS`` is defined as a
sequence. We need to remove the first four items of the sequence and
add ``'hello'`` to the end.  Variable ``MIDDLEWARE_CLASSES`` follows,
and in there we need to remove the line containing
``SessionAuthenticationMiddleware``. These two definitions thus
become::

    INSTALLED_APPS = (
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'hello',
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

Our Django site is ready. Start it like this:

.. code-block:: sh

    python manage.py runserver

and then visit http://localhost:8000/ in your browser.

Anatomy of manage.py
--------------------

As you have seen, Django execution begins at ``manage.py``. Django
created this file itself when we executed ``django-admin
startproject``.  So far we have used this script twice: once in order
to create a new app (``python manage.py startapp hello``), and once in
order run the server (``python manage.py runserver``). ``manage.py``
can do many more things, of which you can get an idea by running
``python manage.py help``. You can also try ``python manage.py help
runserver`` to get help for the ``runserver`` subcommand. Here are
some useful variations:

.. code-block:: sh

    python manage.py runserver 8001  # Listen on specified port (8001 in this case)
    python manage.py runserver 0.0.0.0:8001  # Listen on all interfaces

The last one is particularly important because by default the server
listens on the local interface only. Usually this suffices, but
sometimes it does not.

``python manage.py runserver`` is only meant for development. When you
deploy your application with nginx or apache or another web server,
you won't be using ``python manage.py runserver``; instead, you will
be using :file:`my_first_django_project/wsgi.py`. However, for the
time we will stick to using ``python manage.py runserver``.

These are the entire contents of :file:`manage.py`:

.. literalinclude:: examples/chapter_01/my_first_django_project/manage.py

What is important here is that the script sets an environment variable
that specifies the project's configuration file, i.e.
:file:`my_first_django_project/settings.py`. So, to recap, when you
type ``python manage.py runserver``, django reads your project's
configuration file, and then starts a server that is listening on port
8000, waiting for requests. Let's now see what happens when you give
it such a request.

Anatomy of a web request
------------------------

When you fire up your browser and ask it to give you
http://localhost:8000/, your browser makes a request like this to
Django:

.. code-block:: http

    GET / HTTP/1.1
    Host: localhost:8000
    User-Agent: Mozilla/5.0 (X11; Linux i686 on x86_64; rv:33.0) Gecko/20100101 Firefox/33.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate
    Connection: keep-alive

The most important part is the first line: the browser asks to GET the
resource named "/". If you had asked for
http://localhost:8000/blog/18/, the browser would have asked to get
the resource named "/blog/18/". In our case, Django needs to find out
which view is responsible for the resource named "/". It does this by
looking up a table that we call the URLconf.

If you look at the configuration file,
:file:`my_first_django_project/settings.py`, you will find the
following line::

    ROOT_URLCONF = 'my_first_django_project.urls'

This configuration parameter tells Django that our root URLconf is in
file :file:`my_first_django_project/urls.py`. This is one of the files
we created above.  Let's look at it again:

.. literalinclude:: examples/chapter_01/my_first_django_project/my_first_django_project/urls.py

The table that maps resources to views is the contents
of the ``urlpatterns`` variable. We won't go into details now; what
our root URLconf says is that all requests should be handled by
another URLconf: ``hello.urls``:

.. literalinclude:: examples/chapter_01/my_first_django_project/hello/urls.py

This says that the resource named "/" is to be served by
:class:`HomePageView`. (In the URLconf, resources are specified
without the leading slash, so our resource is actually the empty
string, which is matched by r'^$'.) There is no need to understand the
details clearly at this stage; we will deal with it in more detail in
the next chapter.

So now Django knows that the requested page must be served by
:class:`HomePageView`, which is this:

.. literalinclude:: examples/chapter_01/my_first_django_project/hello/views.py

The following things will now take place:

1. Django will construct a :class:`HomePageView` object.
2. Django will call the object's :meth:`dispatch()` method.
3. :meth:`dispatch()` will return a :class:`HTTPResponse` object,
   which Django will use in order to provide the response.

Unit testing
------------

Let's see how to :ref:`unit test <fpp>` our Django app. Remove file
:file:`hello/tests.py`. Instead, create directory :file:`hello/tests`,
an empty file :file:`hello/tests/__init__.py`, and a
:file:`hello/tests/test_views.py`.

In fact, our Django app is so simple that if we just used the file
:file:`hello/tests.py` that Django created for us it would have been
fine. However, your apps will rarely actually be that simple, and you
will practically always create a :file:`tests` directory that will be
containing various test modules. This happens to be standard practice
as well, and it's better to get into that habit right from the start.
We are naming our first test module :file:`test_views.py` because it
tests the functionality of :file:`views.py`; this is also a standard
convention. In any case, it is very important that its name begins
with ``test``.

These should be the contents of :file:`hello/tests/test_views.py`:

.. literalinclude:: examples/chapter_01/my_first_django_project/hello/tests/test_views.py

:class:`django.test.SimpleTestCase` inherits the Python standard
library's :class:`unittest.TestCase`. It adds some Django-specific
functionality. One is the :attr:`client` attribute, which contains an
HTTP client which can create HTTP requests to the Django server. It
also adds some extra assertion methods, of which we have used one
here. The rest should be self-explanatory.

You can run the unit tests simply like this:

.. code-block:: sh

   python manage.py test
