"""
This module deals with generating a random list, and using
merge sort to produce a sorted version of the same
"""

import rand


def merge_sort(arr):
    """
    This function will return a sorted version of the input list

    Args:
        arr: the list to be sorted

    Returns:
        Sorted version of the original list
    """
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    This function combines two sorted lists (left_arr and right_arr)
    to return a single sorted list

    Args:
        left_arr: sorted list to be combined with another
        right_arr: sorted list to be combined with another

    Returns:
        Combined and sorted version of the two sorted lists
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[left_index + right_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[left_index + right_index] = right_arr[right_index]
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + i] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[i + right_index] = left_arr[i]

    return merge_arr


random_array = rand.random_array([None] * 20)
arr_out = merge_sort([])

print(arr_out)
