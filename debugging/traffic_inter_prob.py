# ns means north south
# ew means east west
market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(intersection):
    # the key can be ns or ew
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'

    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)


# The code below gives output
'''
I/P: {'ns': 'green', 'ew': 'red'}
O/P: {'ns': 'yellow', 'ew': 'green'}
this means traffic keeps moving in both directions

so we add assert statement to capture this before hand

- if assert fails the program must crash, 
- failing fast means we shorten the time bw the original cause of the bug and when ou notice the bug
- Assertions are for detecting programmer errors that are not meant to be recovered from.
- User errors should raise exceptions.
'''
print(market_2nd)
switchLights(market_2nd)
print(market_2nd)