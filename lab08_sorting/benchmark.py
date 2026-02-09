import time

import sorting



def measure_bubblesort():
    data = sorting.generate_random_list(1000)
    
    print(f"Сгенерирован список из {len(data)} элементов.")
    

    start_time = time.perf_counter()

    sorting.bubbleSort(data)
    
    end_time = time.perf_counter()
    
    execution_time = end_time - start_time
    print(f"Время выполнения Bubble Sort: {execution_time:.3f} секунд.")

if __name__ == "__main__":
    measure_bubblesort()