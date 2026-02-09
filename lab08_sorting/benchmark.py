import time

import sorting

def measure_sorting_time(sort_func, num_elements: int = 1000, data: list[int] = None) -> float:
    """A universal function for measuring the time of any sorting algorithm."""
    
    if data is None:
        data = sorting.generate_random_list(num_elements)
    
    start_time = time.perf_counter()
    sort_func(data)
    end_time = time.perf_counter()
    
    return end_time - start_time

if __name__ == "__main__":
    try:
        raw_input = input("Enter list length [default 1000]: ")
        num_elements = int(raw_input) if raw_input else 1000
    except ValueError:
        print("Invalid input, using 1000.")
        num_elements = 1000

    data = sorting.generate_random_list(num_elements)

    algorithms = [
        ("Bubble Sort", sorting.bubbleSort),
        ("Selection Sort", sorting.selectionSort),
        ("Quick Sort", sorting.quickSort),
    ]

    print(f"\nMeasuring algorithms with {num_elements} elements:\n")

    for name, func in algorithms:
        exec_time = measure_sorting_time(func, num_elements, data.copy())
        print(f"{name:15}: {exec_time:.5f} seconds")