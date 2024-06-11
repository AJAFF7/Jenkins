from ops import *

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(3, 2) == 1
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(10, 5) == 2
    assert divide(10, -2) == -5
    assert divide(0, 1) == 0

    try:
        divide(10, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero!"
