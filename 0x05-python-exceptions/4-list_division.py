#!/usr/bin/python3


def safe_division(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        print("division by 0")
    except TypeError:
        print("wrong type")
    finally:
        return result


def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            result_list.append(safe_division(my_list_1[i], my_list_2[i]))
        except IndexError:
            print("out of range")
            result_list.append(0)

    return result_list
