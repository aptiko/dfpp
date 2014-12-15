.. _fpp:

========================================
What does "For Python Programmers" mean?
========================================

This tutorial assumes you already know some things. It does not
attempt to teach you Python (I assume you are comfortable with Python
2, Python 3, and six), pip, virtualenv, unit testing, TCP/IP
networking, HTTP, or relational databases. You can hardly be called a
Python Programmer if you don't have good understanding of all these
things. However, if you are missing something, I provide some
pointers.

Python
------

Some people like the official Python Tutorial, but I don't. I learned
Python with Python Essential Reference by D. M. Beazley. I think it
was a great book, but it was suitable only for experienced
programmers. If you are not an experienced programmer, maybe you need
another book - there is a large number of such books on the market;
you have to choose. If you are an experienced programmer, maybe the
newer editions of Beazley are still great, but I don't really know
since I haven't read them.

Python 2 vs. Python 3, and six
------------------------------

It is my opinion that everyone should learn Python 3 and that it
should be used in all new projects. If you are an experienced Python 2
programmer, make sure you learn Python 3. If you don't know Python
yet, make sure the book you choose teaches you Python 3. If it teaches
you both 2 and 3, so much the better.

In this tutorial the examples run both with 2 and 3, and for that they
use six_.

.. _six: http://pythonhosted.org/six/

pip and virtualenv
------------------

pip_, practically speaking, is Python's package manager.  For this
tutorial, you don't need to know how to package your own code, but you
need to be able to install and manage stuff with pip. virtualenv_ is a
tool every Python programmer should be familiar with.  After you
become comfortable with it, virtualenvwrapper_ will make you life even
easier.

.. _pip: https://pip.pypa.io/en/latest/
.. _virtualenv: https://virtualenv.pypa.io/en/latest/
.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/en/latest/

Unit testing
------------

There is so much urging on the net about the importance of unit
testing that I have absolutely nothing to add. I assume you are
familiar with the Python unittest standard library module.

TCP/IP networking and HTTP
--------------------------

Django is used to create web applications, and web applications are
client-server applications where the client communicates with the
server with HTTP, which is a protocol built on top of TCP, which is a
protocol built on top IP. It's hard to develop web applications if you
don't understand all that very clearly.

If you have studied computing, you probably took one or two courses on
computer networks and you should know all that already. If you don't,
it will be very useful to find a good book and learn.

Relational databases
--------------------

The problem with relational databases is that everyone will tell you
they know them, when in fact very few people do. Same thing with
books. Anyway, you should be comfortable at least with the third
normal form. I've found Practical Issues in Database Management, by
Fabian Pascal, to be quite helpful.  I think that the word "practical"
in the title is meant to tell you that you can understand it, because
it approaches the issues from a practical point of view, it doesn't
use relational calculus. However, it is theoretical in the sense that
it will tell you few solutions to your real problems; but it will help
your mind think in the proper way. Don't be misled into thinking it's
old - what the heck, it is more than 10 years younger than the second
edition of K&R. It's much more likely for this tutorial to be outdated
than for such books.
