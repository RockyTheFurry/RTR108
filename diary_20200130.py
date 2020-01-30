Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: /home/user/RTR108/python_tests.py =================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_tests.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_tests.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_tests.py', 'a': 10}
>>> 
================= RESTART: /home/user/RTR108/python_tests.py =================
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_tests.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_tests.py'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/home/user/RTR108/python_tests.py', 'a': 10}
Traceback (most recent call last):
  File "/home/user/RTR108/python_tests.py", line 8, in <module>
    print(cos(a))
NameError: name 'cos' is not defined
>>> _builtins_.
SyntaxError: invalid syntax
>>> __builtins__.__doc__
"Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices."
>>> print(__builtins__.__doc__)
Built-in functions, exceptions, and other objects.

Noteworthy: None is the `nil' object; Ellipsis represents `...' in slices.
>>> print(a.__doc__)
int(x=0) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4
>>> 
================= RESTART: /home/user/RTR108/python_tests.py =================
Traceback (most recent call last):
  File "/home/user/RTR108/python_tests.py", line 8, in <module>
    print(cos(a))
NameError: name 'cos' is not defined
>>> 
================= RESTART: /home/user/RTR108/python_tests.py =================
-0.8390715290764524
>>> 
================= RESTART: /home/user/RTR108/python_tests.py =================
-0.8390715290764524
0.40808206181339196
>>> 
================= RESTART: /home/user/RTR108/python_tests.py =================
-0.8390715290764524
0.40808206181339196
0.40808206181339196
>>> 
================= RESTART: /home/user/RTR108/python_tests.py =================
-0.8390715290764524
0.40808206181339196
0.40808206181339196
-0.34737226057332327
>>> 
================= RESTART: /home/user/RTR108/python_tests.py =================
-0.8390715290764524
0.40808206181339196
0.40808206181339196
-0.34737226057332327
-0.34737226057332327
>>> 
