from hello import add


def test_add():
    x = 2
    y = 3
    result = add(2, 3)
    assert result == 5
