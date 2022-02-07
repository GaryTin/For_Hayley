
def partition(data, low, high) -> int:
    i = low - 1
    pivot = data[high]
    for j in range(low, high):
        if data[j] <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[high] = data[high], data[i + 1]
    return (i + 1)

def quickSort(data, low, high):
    if len(data) == 1:
        return data
    if low < high:
        pi = partition(data, low, high)
        quickSort(data, low, pi - 1)
        quickSort(data, pi + 1, high)

data = [10, 4, 5, 2, 0, 3]
n = len(data)
quickSort(data, 0, n - 1)
print(data)
