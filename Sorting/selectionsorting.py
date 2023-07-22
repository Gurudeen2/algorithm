def selectionsorting(array):
    size = len(array)

    for step in range(size):
        index = step
        for i in range(index+1, size):
            if array[i] < array[index]:
                array[i], array[index] = array[index], array[i]
    return array

print(selectionsorting([7,9,1,4,0]))