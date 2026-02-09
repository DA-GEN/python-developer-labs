def task1(words_list):
    if words_list:
        average = sum(words_list) / len(words_list) 
        
        print(f'Length of the list: {len(words_list)}')
        print(f'Middle of the list: {average}')
        print(f'Reversed list: {words_list[::-1]}')
    else:
        print('Error: list is empty. Please try again.')
        return task1(list(map(int, input("Enter num list: ").split())))

def task2(key):
    menu = {
        "apple": 10,
        "banana": 5,
        "orange": 8
    }
    
    if key in menu: 
        print(menu[key])
    else:
        print('Error: wrong element. Please try again.')
        print("Available keys:", *menu.keys()) 
        return task2(str(input("Enter the key: ")))

def task3(words_list):
    if words_list:
        word_counts = {}
        PUNCTUATION = '.,!?"'
        
        for raw_word in words_list:
            clean_word = raw_word.strip(PUNCTUATION).lower() 
            
            if clean_word:
                word_counts[clean_word] = word_counts.get(clean_word, 0) + 1
        
        print("\n--- Word Counts ---")
        for key, value in word_counts.items():
            print(f"{key} - {value}")
            
    else:
        print("The sentence is empty. Please try again.")
        return task3(input('Enter a sentence: ').lower().split())

def main():
    print('\n-----Task 1-----')
    try:
        input_list = list(map(int, input("Enter num list: ").split()))
    except ValueError:
        print("Invalid input: Please enter only numbers separated by spaces.")
        task1(list(map(int, input("Enter num list: ").split())))
        
    task1(input_list)

    print('\n-----Task 2-----')
    task2(input("Enter the key: ").strip().lower())

    print('\n-----Task 3-----')
    task3(input('Enter a sentence: ').lower().split())

if __name__ == "__main__":
    main()