# You are to write a function which takes a sorted list and an integer k and return True if any pair of numbers add up to k and False otherwise.
# However, your solution should be O(n).


def sum_to_k(lst, k):
    i = 0
    j = len(lst) - 1
    while i != j:
        if lst[i] + lst[j] < k:
            i += 1
        elif lst[i] + lst[j] > k:
            j -= 1
        else:
            return True
    return False
