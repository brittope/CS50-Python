from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12

    jar = Jar(capacity=15)
    assert jar.size == 0
    assert jar.capacity == 15
    with pytest.raises(ValueError, match='The capacity must be bigger than zero'):
        Jar(capacity=-5)

def test_str():
    jar = Jar()
    assert str(jar) == ''
    jar.deposit(1)
    assert str(jar) == '🍪'
    jar.deposit(5)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪'

def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    with pytest.raises(ValueError, match= 'Too much cookies'):
        jar.deposit(13)

def test_withdraw():
    jar = Jar()
    jar.deposit(2)
    jar.withdraw(1)
    assert jar.size == 1
    with pytest.raises(ValueError, match='Not enough cookies'):
        jar.withdraw(2)

def test_capacity_property():
    jar = Jar()
    assert jar.capacity == 12
    jar.capacity = 15
    assert jar.capacity == 15
    jar.capacity = 12.5
    with pytest.raises(ValueError, match='The capacity must be bigger than zero'):
        jar.capacity = -5

def test_size_property():
    jar = Jar()
    assert jar.size == 0
    jar.size = 8
    assert jar.size == 8
    with pytest.raises(ValueError, match='The size must be between zero and 12'):
        jar.size = 20
