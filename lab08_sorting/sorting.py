import random



def generate_random_list(size: int = 1000) -> list[int]:
    """Generates a list of random integers of the specified size."""

    array = []

    for i in range(size):
        array.append(random.randint(1, 10000))
    
    return array


def bubbleSort(array: list[int], reverse:bool = False) -> list[int]:
    """Sorts a list using the bubble sort method with direction support."""

    arrayLen = len(array)
    
    for i in range(arrayLen):
        swapped = False
        
        for j in range(0, arrayLen - i - 1):
            should_swap = array[j] < array[j+1] if reverse else array[j] > array[j+1]
            
            if should_swap:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        
        if not swapped:
            break
    
    return array

def selectionSort(array: list[int], reverse:bool = False) -> list[int]:
    """Sorts a list using the selection sort method with direction support."""

    arrayLen = len(array)
    
    for i in range(arrayLen):
        selected_index = i
        
        for j in range(i+1, arrayLen):
            should_select = array[j] < array[selected_index] if reverse else array[j] > array[selected_index]
            
            if should_select:
                selected_index = j
        
        if selected_index != i:
            array[i], array[selected_index] = array[selected_index], array[i]
    
    return array


def quickSort(array: list[int], reverse:bool = False) -> list[int]:
    """Sorts a list using the quick sort method with direction support."""

    if len(array) <= 1:
        return array
    
    pivot = array[len(array) // 2]
    
    left = [x for x in array if x < pivot] if not reverse else [x for x in array if x > pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot] if not reverse else [x for x in array if x < pivot]
    
    return quickSort(left, reverse) + middle + quickSort(right, reverse)

if __name__ == "__main__":
    data = generate_random_list(1000)
    
    print(f'\nBubble sort: \n{bubbleSort(data)}')
    
    print(f'\nSelection sort: \n{selectionSort(data)}')
    
    print(f'\nQuick sort: \n{quickSort(data)}')