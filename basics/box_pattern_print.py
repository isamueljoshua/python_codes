"""
print the below pattern

*************
*           *
*           *
*           *
*************
"""

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1.')

    if (width < 2) or (height < 2):
        raise Exception('"width" and "height" must be greater than or equal to 2')

    # Print the first row in pattern
    print(symbol * width)

    # running loop for height - 2 since we are leaving out the first and last row
    for i in range(height - 2):
        # width - 2 since the first and last columns is filled by the symbol
        print(symbol + (' ' * (width - 2)) + symbol)
    
    # Print the last row in pattern
    print(symbol * width)

boxPrint('*', 13, 5)
# boxPrint('*', 1, 1)
# boxPrint('**', 13, 5)
