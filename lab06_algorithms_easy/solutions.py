# Input Functions
def get_int_list(word:str = "Enter list of numbers: ") -> list[int]:
    return list(map(int,input(word).split()))    

def get_str_list(word:str = "Enter list: ") -> list[int]:
    return list(map(str,input(word).split()))    

def get_int(word:str = "Enter a number: ") -> int:
    return int(input(word))

def get_str(word:str = "Enter a string: ") -> str:
    return str(input(word))


# Reverse String
def reverseList(s: list[str]) -> list[str]:
    left = 0
    right = len(s)-1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


# Two Sum
def twoSum(nums: list[int], target: int) -> list[int]:
    prevMap = {} 
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i


# FizzBuzz 
def fizzBuzz(n: int) -> list[str]:
    answer = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    return answer


# Contains Duplicate
def containsDuplicate(nums: list[int]) -> bool:
    seen = set()
    
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
        
    return False


# Valid Anagram
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


# Maximum Subarray
def maxSubArray(nums: list[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
        
    return max_sum


# Move Zeroes
def moveZeroes(nums: list[int]) -> list[int]:
    last_non_zero = 0

    for cur in range(0, len(nums)):
       if nums[cur] != 0:
           nums[last_non_zero], nums[cur] = nums[cur], nums[last_non_zero]
           last_non_zero +=1

    return nums


# Plus One
def plusOne(digits: list[int]) -> list[int]:
    status = True
    cur = len(digits)-1
    while status:
        digits[cur] += 1
        if digits[cur] == 10:
            digits[cur] = 0
            if cur != 0:
                cur -= 1
            else:
                digits.append(1)
                for i in range(1, len(digits)):
                    digits[0], digits[i] = digits[i], digits[0]
                status = False
        else:
            status = False    
    return digits


# Merge Two Sorted Lists
# Class Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Creating linked list by usual list
def createLL(arr: list[int]) -> ListNode:
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
        
    return head

# Printing linked list
def printLL(node: ListNode) -> None:
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print(" -> ".join(res))       

# Merge Two Sorted Lists main function
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 if list1 else list2
        
        return dummy.next


# Intersection of Two Arrays
def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        return list(set1 & set2)



def main():
    # Reverse String
    print("\n---Reverse String---")
    print(reverseList(get_str_list()))

    # Two Sum
    print("\n---Two Sum---")
    print(twoSum(get_int_list(), get_int("Enter a target number: ")))
    
    # FizzBuzz
    print("\n---FizzBuzz---")
    print(fizzBuzz(get_int()))

    # Contains Duplicate
    print("\n---Contains Duplicate---")
    print(containsDuplicate(get_int_list()))

    # Valid Anagram
    print("\n---Valid Anagram---")
    print(isAnagram(get_str("Enter first word: "), get_str("Enter second word: ")))

    # Maximum Subarray
    print("\n---Maximum Subarray---")
    print(maxSubArray(get_int_list()))
    
    # Move Zeroes
    print("\n---Move Zeroes---")
    print(moveZeroes(get_int_list()))
    
    # Plus One
    print("\n---Plus One---")
    print(plusOne(get_int_list("Enter list of numbers one by one symbol: ")))

    # Merge Two Sorted Lists
    print("\n---Merge Two Sorted Lists---")
    printLL(mergeTwoLists(createLL(get_int_list()), createLL(get_int_list())))

    # Intersection of Two Arrays
    print("\n---Intersection of Two Arrays---")
    print(intersection(get_int_list(), get_int_list()))


    print("\n---Done---\n")


if __name__ == "__main__":
    main()