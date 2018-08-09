# from chatlogic import answer
from chatlogic import vm
# def test_plus():
#     # assert 1+2 == 3
#     expected = "불렀어?"
#     actual = answer("민경")
#     assert expected == actual
#

# def test_should_answer_when_called():
#     expected = "불렀어?"
#     actual = answer("민경")
#     assert expected == actual
#
#
# def test_roll_a_die():
#     expected = {"1", "2", "3", "4", "5", "6"}
#     actual = set()
#     for i in range(1000):
#         actual.add(answer("주사위"))
#     assert expected == actual
#
# def test_do_nothing_for_unknown_patterns():
#     actual = answer("엉엉")
#     assert actual is None

def test_insert_coin():
    expected = "100원을 넣었습니다."
    actual = vm("동전 100")
    assert expected == actual

def test_change():
    expected = "잔액은 0원입니다."
    actual = vm("잔액")
    assert expected == actual
































#pipenv run pytest test.py
