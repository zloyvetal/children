# write your code here
import pytest


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def what_to_do(data: list) -> int:
    stat_man = True
    value = data
    number = int()
    b = []
    for x in value:
        if is_int(x):
            b.append(int(x))
        else:
            b.extend(x)

    value = b

    for i in value:
        if type(i) == int:
            if stat_man:
                number += i
            elif not stat_man:
                number -= i
        elif type(i) != int:
            if i == '+':
                stat_man = True
            elif i == '-':
                if stat_man:
                    stat_man = False
                elif not stat_man:
                    stat_man = True
    return number


def main():
    checking = True

    while checking:
        input_value = input().split(" ")

        if input_value[0] == '/exit':
            print('Bye!')
            checking = False
            break
        elif input_value[0] == '/help':
            print('The program calculates the addition  and subtraction  of numbers')

        else:
            print(what_to_do(input_value))


def test_1():
    data = list("1+2+3+4")

    assert what_to_do(data) == 10


def test_2():
    data = list("1-2-3")

    assert what_to_do(data) == -4


def test_3():
    data = list("1--2-3")

    assert what_to_do(data) == 0


def test_4():
    data = list("1+-2-+3--4++5++-6")

    assert what_to_do(data) == -1


def test_5():
    data = list("-1-1-1")

    assert what_to_do(data) == -3


@pytest.mark.parametrize("test_input, expected", [("1+2+3+4", 10),
                                                  ("1-2-3", -4),
                                                  ("1--2-3", 0),
                                                  ("1+-2-+3--4++5++-6", -1),
                                                  ("-1-1-1", -3)])
def test_all(test_input, expected):
    assert what_to_do(list(test_input)) == expected


if __name__ == '__main__':
    main()
