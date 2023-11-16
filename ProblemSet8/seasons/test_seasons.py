import pytest
from seasons import seasons, conversor

def test_seasons():
    assert seasons("2004-07-23") == "Ten million, one hundred fifty-seven thousand, seven hundred sixty minutes"
    with pytest.raises(SystemExit):
        seasons("invalid_date")

def test_conversor():
    assert conversor(100) == "One hundred minutes"
    assert conversor(1000) == "One thousand minutes"
