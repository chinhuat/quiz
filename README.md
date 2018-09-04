Python + Docker Quiz
====================

**Goal:** Implement unsigned 16-bit and 32-bit data types in Python which satisfy test cases in `tests` directory, then build the smallest possible container to allow anyone to run the test cases. Please fork this repo on GitHub, then commit and push your changes to your own GitHub account for review.

**Note:** Don't use NumPy (http://www.numpy.org) as it would take away all the fun :-)

**Tip:** Some basic Python concepts or software development practices that might be helpful: operator/method overloading, (python) 2 vs 3, modules or packages, object-oriented programming, test-driven development.

The test cases should produce output messages that looks something like the following:

```
============================= test session starts ==============================
platform linux -- Python 3.7.0, pytest-3.7.4, py-1.6.0, pluggy-0.7.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /root, inifile:
collecting ... collected 8 items

tests/test_UInt16.py::test_UInt16_constructor PASSED                     [ 12%]
tests/test_UInt16.py::test_UInt16_add_int PASSED                         [ 25%]
tests/test_UInt16.py::test_int_add_UInt16 PASSED                         [ 37%]
tests/test_UInt16.py::test_UInt16_add_UInt16 PASSED                      [ 50%]
tests/test_UInt32.py::test_UInt32_constructor PASSED                     [ 62%]
tests/test_UInt32.py::test_UInt32_add_int PASSED                         [ 75%]
tests/test_UInt32.py::test_int_add_UInt32 PASSED                         [ 87%]
tests/test_UInt32.py::test_UInt32_add_UInt32 PASSED                      [100%]

=========================== 8 passed in 0.05 seconds ===========================
```
