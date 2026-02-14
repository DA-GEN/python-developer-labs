import pytest
import src.solutions  


#  Valid Anagram
@pytest.mark.parametrize("input1_str, input2_str, expected", [
    ("radar", "darar", True),
    ("python", "npython", False),
    ("", "", True),
    ("A man a plan", "nA man a plan", False),
    ("12321", "12321", True)
])

def test_is_anagram(input1_str, input2_str, expected):
    assert src.solutions.is_anagram(input1_str, input2_str) == expected


# Contains Duplicate
@pytest.mark.parametrize("arr, expected", [
    ([3, 2, 1], False),
    ([1], False),
    ([1, 1, 2, 3], True),
    ([5, 5, 5], True),
    ([-1, -5, 0], False)
])

def test_containsDuplicate(arr, expected):
    assert src.solutions.containsDuplicate(arr) == expected


# Reverse String
@pytest.mark.parametrize("arr, expected", [
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    (["r", "a", "c", "e", "c", "a", "r"], ["r", "a", "c", "e", "c", "a", "r"]),
    ([], []),
    (["x"], ["x"])
])

def test_reverseList(arr, expected):
    assert src.solutions.reverseList(arr) == expected


# Maximum Subarray
@pytest.mark.parametrize("arr, expected", [
    ([-2,1,-3,4,-1,2,1,-5,4], 6),
    ([1], 1),
    ([5,4,-1,7,8], 23),
    ([-1], -1),
    ([-2,-3,-1], -1)
])

def test_maxSubArray(arr, expected):
    assert src.solutions.maxSubArray(arr) == expected


# Move Zeroes
@pytest.mark.parametrize("arr, expected", [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([0], [0]),
    ([1,2,3], [1,2,3]),
    ([0,0,0], [0,0,0]),
    ([4,2,4,0,0,3,0,5,1], [4,2,4,3,5,1,0,0,0])
])
def test_moveZeroes(arr, expected):
    assert src.solutions.moveZeroes(arr) == expected


