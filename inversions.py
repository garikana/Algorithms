#!/usr/bin/python
import sys
""" counting inversions in an array of integers
The divide and conquer approach is as given below
* total no of inversions = inversions in the left half + inversions in the right half + inversions between left & right arrays
* the key insight here is if the left and right subarrays were sorted, then inversions between them could be counted in O(n) as below.
* if i elem of left > j elem of right, then all elems after i will be greater(sorted left array). 
* so the algorithm is similar to merge-sort, except we also count inversions during the merge procedure
"""

def merge_count(l,r):
    # l, r are left and right sorted arrays
    # we return the sorted array l+r & also update the inversion count
    global inv_count
    i = 0; j = 0
    a = []
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            a.append(l[i])
            i=i+1
        else:
            a.append(r[j])
            j=j+1
            inv_count = inv_count + len(l)-i
    if i < len(l):
        a.extend(l[i:])
    else:
        a.extend(r[j:])
    return a
        
def count_inversions(a):
    # returns the total inversion count of array a
    # len is length of array a

    # base case
    if len(a) == 1:
        return a
    
    l = count_inversions(a[:len(a)/2])
    r = count_inversions(a[len(a)/2:])
    a = merge_count(l,r)
    return a


inv_count = 0
#inp = ['2','10','3','1','-5','0']
#inp = ['1', '2']
inp = sys.stdin.readlines()
inp = list(map(int, inp))

count_inversions(inp)
print(inv_count)
