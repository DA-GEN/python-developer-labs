import os

def task1(num1, num2):
    try: return num1/num2
    except ZeroDivisionError:
        return "error: division by zero"

def task2(filename):
    try:
        script_dir = os.path.dirname(__file__)
        input_file_path = os.path.join(script_dir, filename)
        with open(input_file_path, newline='') as openedfile:
            return "file has been opened"
    except FileNotFoundError:
        return "error: no such file in derictory"

def task3(l):
    try: return l[0]
    except IndexError:
        return "error: empty list"

def main():
    print("-----TASK 1-----")
    num1, num2 = map(int, input("Enter two numbers: ").split())
    print(task1(num1, num2))

    print("-----TASK 2-----")
    print(task2(str(input("Enter file name: "))))

    print("-----TASK 3-----")
    print(task3(str(input('Enter list: ')).split()))
    
if __name__ == "__main__":
    main()