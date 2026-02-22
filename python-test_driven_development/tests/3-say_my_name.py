The ``say_my_name`` function prints a formatted string.

Import:

    >>> say_my_name = __import__('3-say_my_name').say_my_name

It prints with first and last name:

    >>> say_my_name("John", "Smith")
    My name is John Smith

It prints with default last name (note the trailing space):

    >>> say_my_name("Bob")
    My name is Bob 

Type checking for first_name:

    >>> say_my_name(12, "White")
    Traceback (most recent call last):
    TypeError: first_name must be a string

Type checking for last_name:

    >>> say_my_name("John", 42)
    Traceback (most recent call last):
    TypeError: last_name must be a string
