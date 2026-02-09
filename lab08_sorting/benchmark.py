import time

import sorting



def measure_bubblesort(num_elements: int = 1000) -> float:
    """Measures the execution time of the Bubble Sort algorithm."""

    data = sorting.generate_random_list(num_elements)

    start_time = time.perf_counter()
    sorting.bubbleSort(data)
    end_time = time.perf_counter()
    
    execution_time = end_time - start_time
    return float(f"{execution_time:.5f}")


def measure_selectionsort(num_elements: int = 1000) -> float:
    """Measures the execution time of the Selection Sort algorithm."""

    data = sorting.generate_random_list(num_elements)
    
    start_time = time.perf_counter()
    sorting.selectionSort(data)
    end_time = time.perf_counter()
    
    execution_time = end_time - start_time
    return float(f"{execution_time:.5f}")


def measure_quicksort(num_elements: int = 1000) -> float:
    """Measures the execution time of the Quick Sort algorithm."""

    data = sorting.generate_random_list(num_elements)
    
    start_time = time.perf_counter()
    sorting.quickSort(data)
    end_time = time.perf_counter()
    
    execution_time = end_time - start_time
    return float(f"{execution_time:.5f}")

if __name__ == "__main__":
    num_elements = 1000  # You can change this value to test with different sizes

    num_elements = int(input("Enter the list length. If you want to leave the default 1000, press Enter: ") or num_elements)

    print(f"\nMeasuring sorting algorithms with {num_elements} elements:\n")

    print(f"Bubble Sort: {measure_bubblesort(num_elements)} seconds")
    print(f"Selection Sort: {measure_selectionsort(num_elements)} seconds")
    print(f"Quick Sort: {measure_quicksort(num_elements)} seconds")


