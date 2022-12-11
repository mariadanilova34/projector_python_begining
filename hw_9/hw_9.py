# 136. Single Number
#
# Companies
# Given a non-empty array of integers nums, every element appears
# twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime
# complexity and use only constant extra space.

def single_number(numbers: list[int]) -> int:
    set_with_unique_numbers = set()
    for n in numbers:
        if n in set_with_unique_numbers:
            set_with_unique_numbers.remove(n)
        else:
            set_with_unique_numbers.add(n)
    return set_with_unique_numbers.pop()


print(single_number([1, 1, 3, 2, 4, 2, 4]))


def test_single_number():

    result1 = single_number([2, 2, 1])
    assert result1 == 1

    result1 = single_number([4, 1, 2, 1, 2])
    assert result1 == 4

    result1 = single_number([1])
    assert result1 == 1


test_single_number()

# 414. Third Maximum Number
# Given two strings s and t, return true
# if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging
# the letters of a different word or phrase,
# typically using all the original letters exactly once.


def anagram_str(s: str, t: str) -> bool:

    counter_s = {}
    counter_t = {}
    if len(s) != len(t):
        return False
    for letter in s:
        if letter not in counter_s:
            counter_s[letter] = 0
        counter_s[letter] += 1

    for letter_2 in t:
        if letter_2 not in counter_t:
            counter_t[letter_2] = 0
        counter_t[letter_2] += 1

    if dict(sorted[counter_s]) != dict(sorted[counter_t]):
        return False
    else:
        return True


def test_anagram_str():

    result_1 = anagram_str("anagram", "nagaram")
    assert result_1 is True

    result_2 = anagram_str("rat", "car")
    assert result_2 is False


test_anagram_str()


# 414. Third Maximum Number
# Given an integer array nums, return the third distinct
# maximum number in this array.
# If the third maximum does not exist, return the maximum number.

def third_max(nums: list[int]) -> int:
    arr = sorted(set(nums))
    print(arr)
    if len(arr) < 3:
        return arr[-1]
    return arr[-3]


def test_third_max():

    result_test_third_max_1 = third_max([3, 2, 1])
    assert result_test_third_max_1 == 1

    result_test_third_max_2 = third_max([1, 2])
    assert result_test_third_max_2 == 2

    result_test_third_max_3 = third_max([2, 2, 3, 1])
    assert result_test_third_max_3 == 1


test_third_max()
