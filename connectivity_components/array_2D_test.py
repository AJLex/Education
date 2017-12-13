from array_2D import f


def test_f():
    data = [[0, 0], [0, 1], [1, 1], [2, 1], [3, 1], [3, 0], [5, 5], [4, 5], [6, 5]]
    assert f(data, [0,0]) == [[0, 0], [0, 1], [1, 1], [2, 1], [3, 1], [3, 0]]
    assert f(data, [4, 5]) == [[4, 5], [5, 5], [6, 5]]
    data = []
    assert(data, []) == [[], None] 