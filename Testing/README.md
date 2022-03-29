# UNITTEST
This is one of many ways to execute the unittest test runner. When you have a single test file named test_sum.py, calling python test_sum.py is a great way to get started.


Another way is using the unittest command line. This will execute the same test module (called test) via the command line. Try this

`
$ python -m unittest test_sum
`

<br>

Instead of providing the name of a module containing tests, you can request an auto-discovery using the following. This will search the current directory for any files named test*.py and attempt to test them.

`
$ python -m unittest discover
`

<br>

Once you have multiple test files, as long as you follow the test*.py naming pattern, you can provide the name of the directory instead by using the -s flag and the name of the directory

`
$ python -m unittest discover -s tests
`

<br>

Lastly, if your source code is not in the directory root and contained in a subdirectory, you can tell unittest where to execute the tests so that it can import the modules correctly with the -t flag

`
$ python -m unittest discover -s tests -t src
`