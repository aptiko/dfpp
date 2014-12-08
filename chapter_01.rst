======================
Chapter 1: Hello world
======================

The objective of this chapter is to create a web server that listens
on a TCP port and responds with "Hello, world!" and some dynamic
infomration when the server root (i.e. the path "/") is requested.

Pure Python
-----------

First, let's see how we can do it with pure Python before going on to
do it with Django.

.. literalinclude:: examples/chapter_01/hello_pure_python

If you execute this program and visit http://localhost:8000/ with your
browser, you should see it in action.

Installing Django and creating a project and app
------------------------------------------------

Doing the same thing with Django is considerably more complicated (but
it scales; whereas if we added functionality to the pure python
version it would become chaotic very soon).

First, make sure you have Django installed. Assuming you are using
``virtualenv``, a simple ``pip install django`` should suffice.

Next, we need to create a Django project and a Django app::

    django-admin startproject my_first_django_project
    cd my_first_django_project
    ./manage.py startapp hello

We now have a project named ``my_first_django_project`` and an app
named ``hello``. The concept of a Django app is a big discussion which
we will leave for later. For now we can make the simplifying
assumption that a project consists of one or more apps.

When we executed ``./manage.py startapp hello``, Django created
a directory :file:`hello` with several files. In this first chapter we
will not be using some of these files, so it's better to get them out
of the way::

    rm -r hello/admin.py hello/models.py hello/migrations

Writing the code
----------------

First, edit :file:`hello/views.py` so that it contains this:

.. literalinclude:: examples/chapter_01/my_first_django_project/hello/views.py

If you've met the term "view" in the past, beware: Django's usage of
the term might be completely different from what you've seen. Some
texts use the term "controller" or "logic" instead, and they use
"view" or "presentation" for what Django calls a template.  In Django
parlance, a view is a Python class (or a Python function, but this is
legacy).

Then, create directory :file:`hello/templates`, and in there create
file :file:`home.html`, with the following contents:

.. literalinclude:: examples/chapter_01/my_first_django_project/hello/templates/home.html
   :language: html

Next, create :file:`hello/urls.py` with the following contents:

.. literalinclude:: examples/chapter_01/my_first_django_project/hello/urls.py

Change :file:`my_first_django_project/urls.py` so that it looks like
this:

.. literalinclude:: examples/chapter_01/my_first_django_project/my_first_django_project/urls.py

Finally, edit :file:`my_first_django_project/settings.py`. Around line
30 a variable called ``INSTALLED_APPS`` is defined as a sequence. We
need to remove the first four items of the sequence and add
``'hello'`` to the end.  Variable ``MIDDLEWARE_CLASSES`` follows, and
in there we need to remove the line containing
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

Our Django site is ready. Start it like this::

    ./manage.py runserver

and then visit http://localhost:8000/ in your browser.

Anatomy of manage.py
--------------------

As you have seen, Django execution begins at ``manage.py``. Django
created this file itself when we executed ``django-admin
startproject``.  So far we have used this script twice: once in order
to create a new app (``./manage.py startapp hello``), and once in
order run the server (``./manage.py runserver``). ``manage.py`` can do
many more things, of which you can get an idea by running
``./manage.py help``. You can also try ``./manage.py help runserver``
to get help for the ``runserver`` subcommand. Here are some useful
variations::

    ./manage.py runserver 8001  # Listen on specified port (8001 in this case)
    ./manage.py runserver 0.0.0.0:8001  # Listen on all interfaces

The last one is particularly important because by default the server
listens on the local interface only. Usually this suffices, but
sometimes it does not.

``./manage.py runserver`` is only meant for development. When you
deploy your application with nginx or apache or another web server,
you won't be using ``manage.py runserver``; instead, you will be using
:file:`my_first_django_project/wsgi.py`. However, for the time we will
stick to using ``./manage.py runserver``.

These are the entire contents of :file:`manage.py`:

.. literalinclude:: examples/chapter_01/my_first_django_project/manage.py

What is important here is that the script sets an environment variable
that specifies the project's configuration file, i.e.
:file:`my_first_django_project/settings.py`. So, to recap, when you
type ``./manage.py runserver``, django reads your project's
configuration file, and then starts a server that is listening on port
8000, waiting for requests. Let's now see what happens when you give
it such a request.

Anatomy of a web request
------------------------

When you fire up your browser and ask it to give you
http://localhost:8000/, your browser makes a request like this to
Django::

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
2. Django will call the object's :meth:`dispatch()` method (this is
   defined in the superclasses of :class:`HomePageView`), passing it
   all necessary information from the HTTP request.
3. :meth:`dispatch()` will return a string which Django will provide
   to the client as the HTTP response.
   
As you can guess, what :meth:`dispatch()` will do is render the
specified template and return the rendered result. The template uses
placeholders like ``{{ my_pid }}`` and ``{{ a_random }}``. When the
template is rendered, these placeholders are replaced by the contents
of the variables ``my_pid`` and ``a_random``. These variables are
specified in a dictionary called *the context*. The job of
:meth:`get_context_data()` is to return a context for rendering the
template.
