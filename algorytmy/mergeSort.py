from kolory.colors import *

def merge(data, start, mid, end):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if p > mid:
            tempArray.append(data[q])
            q+=1
        elif q > end:
            tempArray.append(data[p])
            p+=1
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p+=1
        else:
            tempArray.append(data[q])
            q+=1

    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start += 1

def merge_sort(data, start, end, drawData, window):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(data, start, mid, drawData, window)
        merge_sort(data, mid+1, end, drawData, window)

        merge(data, start, mid, end)

        drawData(data, [PURPLE if x >= start and x < mid else YELLOW if x == mid 
                        else DARK_BLUE if x > mid and x <=end else BLUE for x in range(len(data))])
        window.after(1)

    drawData(data, [BLUE for x in range(len(data))])