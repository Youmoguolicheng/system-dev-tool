from merge_sort import merge_sort

# 题目给定输入
def test_given_input():
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

# 含重复元素的列表
def test_dup_elements():
    assert merge_sort([5,2,2,8,2,1]) == [1,2,2,2,5,8]
