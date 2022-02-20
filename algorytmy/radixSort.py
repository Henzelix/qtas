from kolory.colors import *

def countingSort(data, exp1):
 
    n = len(data)
 
    # The output array elements that will have sorted arr
    output = [0] * (n)
 
    # initialize count array as 0
    count = [0] * (10)
 
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = data[i] // exp1
        count[index % 10] += 1
 
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Build the output array
    i = n - 1
    while i >= 0:
        index = data[i] // exp1
        output[count[index % 10] - 1] = data[i]
        count[index % 10] -= 1
        i -= 1
 
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(data)):
        data[i] = output[i]
 
# Method to do Radix Sort
def radix_sort(data, drawData, window):
 
    # Find the maximum number to know number of digits
    max1 = max(data)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 1:
        countingSort(data, exp)
        exp *= 10
        drawData(data, [YELLOW if x==exp else BLUE for x in range(len(data))])
        window.after(1)

    drawData(data, [BLUE for x in range(len(data))])
    
    print(data)