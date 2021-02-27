#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/2/27 12:25 PM
# @Author: wisdom
# @File:longestIncreasingSubSequence.py


def longestIncreasingSubSequence(lists: list):
    if len(lists) == 0:
        return None
    listResult = []
    for i in range(len(lists)):
        listResult.append(1)
    print(listResult)
    # one dimension array can solve
    # compare  current number with all previous elements
    # when come across one element lower than current elements meaning
    # the longest array contain this words
    for index in range(len(lists)):
        for j in range(0, index):
            if lists[index]>lists[j]:
                listResult[index] = max(listResult[index],listResult[j]+1)
    maxLen = max(listResult)
    return maxLen


if __name__ == '__main__':
    print('longest increasing sub sequence')
    lists = list(map(int, input().split(' ')))
    print(longestIncreasingSubSequence(lists))
