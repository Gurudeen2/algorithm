def selectionsorting(array):
    size = len(array)

    for step in range(size):
        minindex = step
        for i in range(step+1, size):
            if array[i] < array[minindex]:
                minindex = i
        array[step], array[minindex] = array[minindex], array[step]
    return array

print(selectionsorting([-2, 45, 0, 11, -9,88,-97,-202,747]))