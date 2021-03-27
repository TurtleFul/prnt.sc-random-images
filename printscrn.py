import webbrowser as w
import random
import string
import threading


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str


def get_random_digits(length):
    # choose from all lowercase letter
    letters = string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str

def every10():
    threading.Timer(10.0, every10).start()
    randLetters = get_random_string(2)
    randDigits = get_random_digits(4)
    baseUrl = "prnt.sc/"

    finalUrl = baseUrl + randLetters + randDigits
    print(finalUrl)
    w.get("firefox").open(finalUrl)





every10()