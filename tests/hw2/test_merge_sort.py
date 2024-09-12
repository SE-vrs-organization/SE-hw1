import pytest
import sys
import os

# Add the src/hw2 directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))



def test_merge_sort_basic_unsorted_list():
    unsorted_list = [4, 1, 3, 2]
    sorted_list = merge_sort(unsorted_list)
    assert sorted_list == [1, 2, 3, 4]

def test_merge_sort_empty_list():
    unsorted_list = []
    sorted_list = merge_sort(unsorted_list)
    assert sorted_list == []

def test_merge_sort_some_negative_numbers_list():
    unsorted_list = [0, -1, 3, -5, 2]
    sorted_list = merge_sort(unsorted_list)
    assert sorted_list == [-5, -1, 0, 2, 3]

def test_merge_sort_already_sorted_list():
    unsorted_list = [1, 2, 3, 4, 5]
    sorted_list = merge_sort(unsorted_list)
    assert sorted_list == [1, 2, 3, 4, 5]

def test_merge_sort_reverse_sorted_list():
    unsorted_list = [5, 4, 3, 2, 1]
    sorted_list = merge_sort(unsorted_list)
    assert sorted_list == [1, 2, 3, 4, 5]

def test_merge_sort_single_element_list():
    unsorted_list = [42]
    sorted_list = merge_sort(unsorted_list)
    assert sorted_list == [42]

def test_merge_sort_duplicates_values_in_list():
    unsorted_list = [3, 1, 2, 2, 3]
    sorted_list = merge_sort(unsorted_list)
    assert sorted_list == [1, 2, 2, 3, 3]

def test_merge_sort_list_with_large_numbers():
    unsorted_list = [1000000, 1, 50000, 100, 10000]
    sorted_list = merge_sort(unsorted_list)
    assert sorted_list == [1, 100, 10000, 50000, 1000000]

def test_merge_sort_list_with_float_numbers():
    unsorted_list = [1.5, 0.5, 2.5, 3.5, 1.0]
    sorted_list = merge_sort(unsorted_list)
    assert sorted_list == [0.5, 1.0, 1.5, 2.5, 3.5]

def test_merge_sort_large_list():
    unsorted_list = list(range(10000, 0, -1))  
    sorted_list = merge_sort(unsorted_list)
    assert sorted_list == list(range(1, 10001))