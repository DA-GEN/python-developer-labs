# Input Functions
def get_int_list(word: str = "Enter list of numbers: ") -> list[int]:
    """Read a space-separated string of numbers and return a list of integers."""
    return list(map(int, input(word).split()))    


def get_str_list(word: str = "Enter list: ") -> list[str]:
    """Read a space-separated string and return a list of strings."""
    return list(map(str, input(word).split()))    


def get_int(word: str = "Enter a number: ") -> int:
    """Prompt for user input and return it as an integer."""
    return int(input(word))


def get_str(word: str = "Enter a string: ") -> str:
    """Prompt for user input and return it as a string."""
    return str(input(word))


# Reverse String
def reverseList(s: list[str]) -> list[str]:
    """Reverse a list of strings in-place using the two-pointer approach."""
    left = 0
    right = len(s)-1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s


# Two Sum
def twoSum(nums: list[int], target: int) -> list[int]:
    """Find the indices of two numbers that add up to a specific target using a hash map."""
    prevMap = {} 

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i


# FizzBuzz 
def fizzBuzz(n: int) -> list[str]:
    """Return a list of strings where multiples of 3 are 'Fizz', 5 are 'Buzz', and both are 'FizzBuzz'."""
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
    """Return True if any value appears at least twice in the array, using a set for tracking."""
    seen = set()

    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    
    return False


# Valid Anagram
def is_anagram(s: str, t: str) -> bool:
    """Check if two strings are anagrams by comparing their sorted character lists."""
    return sorted(s) == sorted(t)


# Maximum Subarray
def maxSubArray(nums: list[int]) -> int:
    """Find the contiguous subarray with the largest sum using Kadane's Algorithm."""
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum


# Move Zeroes
def moveZeroes(nums: list[int]) -> list[int]:
    """Move all 0s to the end of the list in-place while maintaining the relative order of non-zero elements."""
    last_non_zero = 0

    for cur in range(0, len(nums)):
       if nums[cur] != 0:
           nums[last_non_zero], nums[cur] = nums[cur], nums[last_non_zero]
           last_non_zero +=1
    
    return nums


# Plus One
def plusOne(digits: list[int]) -> list[int]:
    """Increment the large integer represented by a list of digits by one."""
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits


# Merge Two Sorted Lists
# Class Node
class ListNode:
    """A standard node definition for a singly linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Creating linked list by usual list
def createLL(arr: list[int]) -> ListNode:
    """Convert a Python list into a singly linked list and return the head node."""
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
    """Traverse the linked list and print its values in 'val -> next' format."""
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print(" -> ".join(res))       


# Merge Two Sorted Lists main function
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    """Merge two sorted linked lists into one sorted list using a dummy head pointer."""
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
    """Return a list of unique elements found in both input arrays using set intersection."""
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
    print(is_anagram(get_str("Enter first word: "), get_str("Enter second word: ")))

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