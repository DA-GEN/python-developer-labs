import random



def generate_random_list(size: int = 1000) -> list[int]:
    """Generates a list of random integers."""
    return [random.randint(1, 10000) for _ in range(size)]


def bubble_sort(array: list[int], reverse: bool = False) -> list[int]:
    """
    Sorts a list using Bubble Sort algorithm.
    Time Complexity: O(N^2)
    """

    array = array.copy()  # To avoid modifying the original list

    n = len(array)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if (array[j] < array[j+1]) if reverse else (array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

        if not swapped:
            break

    return array


def selection_sort(array: list[int], reverse: bool = False) -> list[int]:
    """
    Sorts a list using Selection Sort algorithm.
    Time Complexity: O(N^2)
    """

    array = array.copy()  # To avoid modifying the original list

    n = len(array)

    for i in range(n):
        idx = i

        for j in range(i + 1, n):
            condition = array[j] > array[idx] if reverse else array[j] < array[idx]
            if condition:
                idx = j

        array[i], array[idx] = array[idx], array[i]

    return array


def quick_sort(array: list[int], reverse: bool = False) -> list[int]:
    """
    Sorts a list using Quick Sort algorithm.
    Time Complexity: O(N log N) on average, O(N^2) in the worst case.
    """

    array = array.copy()  # To avoid modifying the original list
    
    if len(array) <= 1:
        return array
    
    pivot = array[len(array) // 2]
    
    low = [x for x in array if x < pivot]
    mid = [x for x in array if x == pivot]
    high = [x for x in array if x > pivot]
    
    if reverse:
        return quick_sort(high, True) + mid + quick_sort(low, True)
    
    return quick_sort(low, False) + mid + quick_sort(high, False)

if __name__ == "__main__":
    number_of_elements = 1000
    base_data = generate_random_list(number_of_elements)
    
    print(f"\nOriginal: {base_data}")

    print(f"\nBubble:   {bubble_sort(base_data)}")
    print(f"\nSelection:{selection_sort(base_data, reverse=False)}")
    print(f"\nQuick:    {quick_sort(base_data, reverse=True)}")