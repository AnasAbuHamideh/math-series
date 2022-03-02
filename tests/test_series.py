from math_series.series import fibonacci, lucas, sum_series


#Fibonacci
def test1_fibonacci():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected
 
def test2_fibonacci():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test3_fibonacci():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test4_fibonacci():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected

#Lucas
def test1_lucas():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test2_lucas():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test3_lucas():
    actual = lucas(4)
    expected = 7
    assert actual == expected

def test4_lucas():
    actual = lucas(5)
    expected = 11
    assert actual == expected

#sum_series
def test1_sum():
    actual = sum_series(5)
    expected = fibonacci(5)
    assert actual == expected

def test2_sum():
    actual = sum_series(5,0,1)
    expected = fibonacci(5)
    assert actual == expected

def test3_sum():
    actual = sum_series(5,2,1)
    expected = lucas(5)
    assert actual == expected

def test4_sum():
    actual = sum_series(5,3,2)
    expected = 19
    assert actual == expected

def test5_sum():
    actual = sum_series(3,3,2)
    expected = 7
    assert actual == expected