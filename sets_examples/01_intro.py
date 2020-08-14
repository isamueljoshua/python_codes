# fetch average of all elements in the array
def average(array):
    # your code goes here
    arr_set = set(array)
    avg = sum(arr_set)/len(arr_set)
    return avg

if __name__ == '__main__':
    """ 
    Input Format

    The first line contains the integer, N , the total number of plants.
    The second line contains the N space separated heights of the plants.

    Constraints
    0 < N <= 100

    Output Format
    Output the average height value on a single line.

    Input:
    10
    161 182 161 154 176 170 167 171 170 174

    Output:
    169.375
    """
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
