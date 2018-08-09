from chatlogic import answer
# def test_plus():
#     # assert 1+2 == 3
#     expected = "불렀어?"
#     actual = answer("민경")
#     assert expected == actual
#

def test_should_answer_when_called():
    expected = "불렀어?"
    actual = answer("민경")
    assert expected == actual


def test_roll_a_die():
    expected = {"1", "2", "3", "4", "5", "6"}
    actual = set()
    for i in range(1000):
        actual.add(answer("주사위"))
    assert expected == actual

def test_do_nothing_for_unknown_patterns():
    actual = answer("엉엉")
    assert actual is None









































#pipenv run pytest test.py
