def task1(l):    
    print(f'Length of the list: {len(l)}')
    print(f'Middle of the list: {(sum(l)/2)}')
    print(f'Reversed list: {l[::-1]}')
    
    print(' ')

def task2(key):
    menu = {
        "apple": 10,
        "banana": 5,
        "orange": 8
    }

    print(menu[key])

def task3(n):
    
    dict = {}
    for i in n:
        if i in dict:
            dict[i.strip('.,!?"')] += 1
        else:
            dict[i.strip('.,!?"')] = 1
    
    for key, value in dict.items():
        print(f"{key} - {value}")

    
print('-----Task 1-----')
task1(list(map(int, input("Enter num list: ").split())))

print('-----Task 2-----')
task2(str(input("Enter the key: ")))

print('-----Task 3-----')
task3(list(map(str,input('Enter a sentence: ').lower().split())))