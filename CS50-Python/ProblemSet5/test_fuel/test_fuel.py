from fuel import gauge, convert
import pytest

def test_convert():
    assert convert('2/3') == 67
    with pytest.raises(ValueError):
        assert convert('three/four')
        assert convert('2/1')
    with pytest.raises(ZeroDivisionError):
        assert convert('1/0')

def test_gauge():
    assert gauge(1) == 'E'
    assert gauge(0) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(45) == '45%'