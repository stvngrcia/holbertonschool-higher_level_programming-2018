#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for idx in range(list_length):
        try:
            result_list.append(my_list_1[idx] / my_list_2[idx])
        except(TypeError, ZeroDivisionError, IndexError) as err:
            if (isinstance(err, ZeroDivisionError)):
                print("division by 0")
            elif (isinstance(err, TypeError)):
                print("wrong type")
            elif (isinstance(err, IndexError)):
                print("out of range")
            result_list.append(0)
        finally:
            pass
    return result_list
