# Problem location
# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

"""
Input:
The first line contains the number of items, N.
The next N lines contains the item's name and price, separated by a space.
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30

Output:
Print the item_name and net_price in order of its first occurrence.
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20

"""

from collections import OrderedDict

n = int(input("Enter the number of items: "))
if n>0 and n<=100:
    ord_dct = OrderedDict()
    for i in range(n):
        items = input("Enter item and price: ").split()
        print("Items: ", items)
        item_name = items[:-1]
        item_price = int(items[-1])
        print("Item Name: ", item_name)
        print("Item Price: ", item_price)
        cur_key = " ".join(item_name)
        if cur_key not in ord_dct.keys():
            ord_dct[cur_key] = item_price
        else:
            ord_dct[cur_key] = ord_dct[cur_key] + item_price

    print("Final Dict: ", ord_dct)
    print("Final Dict Keys: ", ord_dct.keys())
    print("Final Dict Items: ", ord_dct.items())
    print("Final Dict Values: ", ord_dct.values())


    print("Values in Dict: ")
    for key in ord_dct.keys():
        # print("Current Key: ", key)
        print(key, ord_dct[key])