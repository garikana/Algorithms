#!/usr/local/bin/python3
import random

""" rselect - randomized selection algorithm to find the ith order statistic of
              and unsorted array 
"""

def partition(start,end,p):
    """ O(n) partition algorithm 
        p - index of pivot element
        start, end - starting & ending indexes of sub array to be
                     partitioned
    """
    global a; # global array a
    
    # partition procedure

    temp = a[start]
    a[start] = a[p]
    a[p] = temp

    l = start; m = start+1
    while m <= end:
        if a[m] <= a[start]:
            temp = a[l+1]
            a[l+1] = a[m]
            a[m] = temp
            l = l+1
        m=m+1
    temp = a[l]
    a[l] = a[start]
    a[start] = temp
    return l
        

    

def rselect(start,end,i):
    global a

    # base case
    if start == end:
        return a[start]

    # we convert ith statistic to its index value
    i = start + i - 1
    # select a random pivot elem
    p = random.randrange(start,end+1)
    
    # partition the array around the pivot
    p = partition(start,end,p)
    
    if p == i: # bingo
        return a[i]
    elif p < i: # search in the right partition
        rselect(p+1,end,i-p-1)
    else: # search in the left partition
        rselect(start,p-1,i)
    

a = [34,-1,100,26,-2]
print(rselect(0,len(a)-1,3))
