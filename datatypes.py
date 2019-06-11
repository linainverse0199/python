def main():
    list1 = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    list2 = list([1, 2, 3, 4, 5] * 5)
    list3 = list([1, 2, 3, 4, 5, 6, 7, 8 * 5])
    list4 = list([1, 2, 3, 4, 5, 6, 7, 8, 9, "10"])
    list5 = [1, "2", 3, 4, 5, "6" * 5]
    list6 = list(range(1, 10, 2))
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(list5)
    print(list6)
    print(list1[-1])
    print(list5[2])
    list7 = [1, 2, 3]
    list8 = [2, 1, 3]
    list9 = [1, 2, 3]
    print(list7 == list8)
    print(list7 == list9)


main()
