
#bubblesorting

def bubblessort(array):
    array_len = len(array)

    for i in range(array_len):
    
        for j in range(array_len-i-1):
            if array[j] > array[j+1]:
                print(f"j:{array[j]}, j+1:{array[j+1]}, arraylen:{array_len}")
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubblessort([2,6,1,5]))

