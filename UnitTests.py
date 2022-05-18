import pytest

def exampleTest(x):
    return x + 5

def testexampleAssert():
    assert exampleTest(5) == 10

