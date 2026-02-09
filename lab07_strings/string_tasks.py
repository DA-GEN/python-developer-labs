# String input sunction
def get_str(word: str = "Enter a string: ") -> str:
    """Prompt for user input and return it as a string."""
    return str(input(word))


# Reverse the string
def reverse_string(s: str) -> str:
    """Return a reversed version of the string using slicing."""
    return s[::-1]


# Remove all spaces from a string
def remove_spaces(s: str) -> str:
    """Return the string with all whitespace characters (spaces, tabs, newlines) removed."""    
    return "".join(s.split())

# Count the number of vowels
def count_vowels(s: str) -> int:
    """Count and return the total number of vowels (a, e, i, o, u, y) in the string."""
    count = 0
    vcb = "aeiouy"

    for char in s:
        if char.lower() in vcb:
            count += 1
    
    return count


# Capitalize the first letter of each word
def capitalize_pref(s: str) -> str:
    """Capitalize the first letter of every word and return as a single string."""
    words = []

    for word in s.split():
        words.append(word.capitalize())
    
    return " ".join(words)

# Check if a string is a palindrome
def is_palindrome(s: str) -> bool:
    """Return True if the string reads the same forwards and backwards."""
    s = "".join(s.split()).lower()

    return s == s[::-1]


if __name__ == "__main__":
    # Reverse the string
    print("\n---Reverse the string---")
    print(reverse_string(get_str()))

    # Remove all spaces from a string
    print("\n---Remove all spaces from a string---")
    print(remove_spaces(get_str()))

    # Count the number of vowels
    print("\n---Count the number of vowels---")
    print(count_vowels(get_str()))

    # Capitalize the first letter of each word
    print("\n---Capitalize the first letter of each word---")
    print(capitalize_pref(get_str()))

    # Check if a string is a palindrome
    print("\n---Check if a string is a palindrome---")
    print(is_palindrome(get_str()))

    print("\n---Done---\n")


