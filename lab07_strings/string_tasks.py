# String input sunction
def get_str(word: str = "Enter a string: ") -> str:
    """Prompt for user input and return it as a string."""
    return str(input(word))


# Reverse the string
def reverseStr(s: str) -> str:
    """Return a reversed version of the string using slicing."""
    return s[::-1]


# Remove all spaces from a string
def removeSpaces(s: str) -> str:
    """Return the string with all whitespace characters removed."""
    return s.replace(" ", "")


# Count the number of vowels
def countVowels(s: str) -> int:
    """Count and return the total number of vowels (a, e, i, o, u, y) in the string."""
    count = 0
    vcb = ['a', 'e', 'i', 'o', 'u', 'y']

    for i in s:
        if i.lower() in vcb:
            count += 1
    
    return count


# Capitalize the first letter of each word
def prefCapitalize(s: str) -> str:
    """Capitalize the first letter of every word and return as a single string."""
    sList = s.split()
    newS = ""
    
    for i in sList:
        newS += i.capitalize() + " "
    
    return newS.removesuffix(" ")


# Check if a string is a palindrome
def isPalindrome(s: str) -> bool:
    """Return True if the string reads the same forwards and backwards."""
    return s == s[::-1]


def main():
    # Reverse the string
    print("\n---Reverse the string---")
    print(reverseStr(get_str()))

    # Remove all spaces from a string
    print("\n---Remove all spaces from a string---")
    print(removeSpaces(get_str()))

    # Count the number of vowels
    print("\n---Count the number of vowels---")
    print(countVowels(get_str()))

    # Capitalize the first letter of each word
    print("\n---Capitalize the first letter of each word---")
    print(prefCapitalize(get_str()))

    # Check if a string is a palindrome
    print("\n---Check if a string is a palindrome---")
    print(isPalindrome(get_str()))

    print("\n---Done---\n")


if __name__ == "__main__":
    main()