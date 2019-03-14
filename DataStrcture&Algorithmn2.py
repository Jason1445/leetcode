# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:24:27 2019
排序算法
@author: Jason
"""


def heapify(L,index,i):
    if 2*i+1<=index and L[2*i+1]>L[i]:
        largest = 2*i+1
    else:
        largest = i
    if 2*i+2<=index and L[2*i+2]>L[largest]:
        largest = 2*i+2
    if largest!=i:
        L[largest], L[i] = L[i], L[largest]
        heapify(L,index,largest)

def createHeap(L,index):#用L[0:index+1]建立堆
    for i in range((index-1)//2,-1,-1):
        heapify(L,index,i)

def heapSort(L):
    index = len(L)-1#堆尾下标
    while index>0:
        createHeap(L,index)
        L[index], L[0] = L[0], L[index]
        index -= 1
    return L       



def quickSortCore(L,start,end):
    if start<end:
        mid = L[end]
        i, j = start, end
        while i<j:
            while L[i]<=mid and i<j:
                i += 1
            while L[j]>=mid and i<j:
                j -= 1
            L[i], L[j]=L[j], L[i]
        L[i], L[end]=L[end], L[i]
        quickSortCore(L,start,i-1)
        quickSortCore(L,i+1,end)
    
def quickSort(L):
    quickSortCore(L,0,len(L)-1)
    return L

def merge(L,start,end):
    
    return 

def mergeSortCore(L,start,end):
    if start > end:
        return []
    if start == end:
        return L[0]
    mid = (start+end)//2
    L = mergeSortCore(L,start,mid)
    L = mergeSortCore(L,mid+1,end)
    L = merge(L,start,mid,end)


def mergeSort(L):
    L2 = []
    L = mergeSortCore(L,0,len(L)-1)
    return L



L=[2,1,3,-2,10,4,7,1,-3]
print(heapSort(L))
print(quickSort(L))