# global

globalVar = 10

import moduleFirst
import moduleFirst as account
from moduleFirst import calculate_income
from moduleFirst import *


def main():
    print("Hello, World!")

    # global
    global globalVar
    globalVar = 12

    # local
    var1 = "First variable"
    var2 = 'Second variable'
    var3 = var1.lower() + '  ' + var2.upper() + str(56).lower()
    print(var1, var2, var3)
    print("Income:", moduleFirst.calculate_income(10, 20, 30))
    print("Income:", account.calculate_income(10, 20, 30))
    print("Income:", calculate_income(10, 20, 30))

    # All existed types:
    int1 = 121
    print("int1")
    print(type(int1))
    boolean1 = True
    boolean2 = False
    print("boolean1")
    print(type(boolean1))
    float1 = 12.1
    print("float1")
    print(type(float1))
    complex1 = 12J
    print("complex1")
    print(type(complex1))
    bytes1 = bytes(122)
    print("bytes1")
    print(type(bytes1))
    byteArray1 = bytearray(213)
    print("byteArray1")
    print(type(byteArray1))
    # mutable
    list1 = [1, 2, 3, 4, 5]
    print("list1")
    print(type(list1))
    # = immutable list
    tuple1 = (1, 2, 3, 4, 5)
    print("tuple1")
    print(type(tuple1))
    # mutable
    set1 = {1, 2, 3, 4, 5, 6}
    print("set1")
    print(type(set1))
    # = immutable set
    frozenSet1 = frozenset({1, 2, 3, 4, 5, 6})
    print("frozenSet1")
    print(type(frozenSet1))
    dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}
    print("dict1")
    print(type(dict1))

    def function1():
        print("Hello function1!")
        return None

    function1()
    print(2 + 3)
    print(2 - 3)
    print(2 / 3)
    print(2 // 3)
    print(2 % 3)
    print(2 ** 3)
    print(2 + int("3"))
    print("3" * 2)
    print(round(2 / float("3"), 4))
    # print(2 // "3")
    # print(2 % "3")
    # print(2 ** "3")
    xb = 0b101
    x0 = 0o202
    x_x = 0xaa
    res = xb > x0 and x_x < x0 or not 12 > 14

    def function_if(a, b):
        if a > b:
            print("a > b")
        elif a < b:
            print("elif a < b")
        else:
            print("a = b")
        print("Finish function")

    function_if(10, 20)

    def function_loops(a, b, c=10):
        i = a
        while i < b:
            print("While Iteration : " + str(i))
            i += 2
        for j in range(a, b, 2):
            print("For loop: " + str(j))
            if a > b:
                break
            elif a < b:
                continue
        print(c)
        return c

    print(function_loops(b=10, a=0))
    print(function_loops(0, 10, c=23))

    try:
        int("str")
    except ValueError:
        print("Exception caught")
    except ZeroDivisionError:
        print("Zero division")
    except Exception as e:
        print("Exception general", e)
        raise e
    finally:
        print("Finally")


main()
