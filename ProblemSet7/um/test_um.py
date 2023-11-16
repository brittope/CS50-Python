from um import count

def test_single():
    assert count('um') == 1
    assert count('um?') == 1
    assert count('um.') == 1
    assert count('Um') == 1

def test_phrase():
    assert count('Um, thanks for the album.') == 1

def test_sentence():
    assert count('Um, thanks, um...') == 2
