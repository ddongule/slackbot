import random


def vm(text):
    global coin #

    if text == "동전 100":
        coin = 100
        return "100원을 넣었습니다."
    elif text == "잔액":
        return "잔액은" + srt(coin) + "원입니다."


def answer(text):
    if "민경" in text:
        reply = "불렀어?"
    elif "주사위" == text:
        reply = str(random.randint(1,6))
    else:
        reply = None
    return reply

# def answer(text):
#     if not text.startswith("민경"):
#         return None
