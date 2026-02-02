import os

def task1(num1, num2):
    try: return num1/num2
    except:
        return "error: division by zero"

def task2(filename):
    try:
        script_dir = os.path.dirname(__file__)
        input_file_path = os.path.join(script_dir, filename)
        with open(input_file_path, newline='') as openedfile:
            return "file has been opened"
    except:
        return "error: no such file in derictory"

def task3(l):
    try: return l[0]
    except:
        return "error: empty list"

def main():
    print("-----TASK 1-----")
    print(task1(1, 2))
    print(task1(1, 0))

    print("-----TASK 2-----")
    print(task2("test.txt"))
    print(task2("sdfsdf.txt"))

    print("-----TASK 3-----")
    print(task3([1,2,3]))
    print(task3([]))

if __name__ == "__main__":
    main()