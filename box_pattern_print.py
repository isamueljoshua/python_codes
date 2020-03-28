"""
print the below pattern

*************
*           *
*           *
*           *
*************
"""

def boxPrint(symbol, width, height):
    # Print the first row in pattern
    print(symbol * width)

    # running loop for height - 2 since we are leaving out the first and last row
    for i in range(height - 2):
        # width - 2 since the first and last columns is filled by the symbol
        print(symbol + (' ' * (width - 2)) + symbol)
    
    # Print the last row in pattern
    print(symbol * width)


boxPrint('*', 13, 5)