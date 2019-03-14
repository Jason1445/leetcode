# -*- coding: utf-8 -*-

'''
排序算法汇总
'''
class solution():
    def __init__(self, val=[]):
        self.l = val
    
    #冒泡排序
    def BubbleSort(self):
        for i in range(len(self.l)-1):
            for j in range(len(self.l)-1-i):
                if self.l[j] > self.l[j+1]:
                    self.l[j], self.l[j+1] = self.l[j+1], self.l[j]
        return self.l
    
    #插入排序
    def InertSort(self):
        for i in range(1,len(self.l)):
            for j in range(i,0,-1):
                if self.l[j]<self.l[j-1]:
                    self.l[j], self.l[j-1] = self.l[j-1], self.l[j]
                else:
                    break
        return self.l
    
    #选择排序
    def SelSort(self):
        for i in range(0,len(self.l)-1):
            index = i
            for j in range(i+1,len(self.l)):    
                if self.l[j] < self.l[index]:
                    index = j
            self.l[i], self.l[index] = self.l[index], self.l[i]
        return self.l
            
    
    #快速排序
    def QuickSort(self):
        self.QuickSortCore(self.l,0,len(self.l)-1)
        return self.l
    
    def QuickSortCore(self,L,l,r):
        i = l-1
        if l<r:    
            for j in range(l,r):
                if L[j]<L[r]:
                    i += 1
                    L[i], L[j] = L[j], L[i]
            L[i+1], L[r] = L[r], L[i+1]
            self.QuickSortCore(L,l,i)
            self.QuickSortCore(L,i+2,r)
            
    #归并排序
    def MergeSort(self):
        S = self.l[:]                           #开辟和L相同大小的新空间
        self.MergeSortCore(self.l,0,len(self.l)-1,S)
        return self.l
    
    def MergeSortCore(self,L,l,r,S):
        if l<r:
            q = int((r+l)/2)
            print(l,q,r)
            self.MergeSortCore(L,l,q,S)
            self.MergeSortCore(L,q+1,r,S)
            self.Merge(L,l,q,r,S)
            self.Merge(S,l,q,r,L)
    
    def Merge(self,L,l,q,r,S):
        i, j, k = l, q+1, l
        while k<=r and i<=q and j<=r:
            if L[i]<=L[j]:
                S[k] = L[i]
                i += 1
            else:
                S[k] = L[j]
                j += 1
            k += 1
        while i<=q:
            S[k] = L[i]
            i += 1
            k += 1
        while j<=r:
            S[k] = L[j]
            j += 1
            k += 1
        
    
L = solution([5,2,1,-2,0,3,-1,-8])
#print(L.l)
#print(L.BubbleSort())
#print(L.InertSort())
#print(L.SelSort())
#print(L.MergeSort())

'''
堆heap
'''
class solution3():
    def __init__(self, L):
        self.L = L
        self.size = len(self.L)-1#堆尾指针
        
    def heapSort(self):
        for i in range(len(self.L)-1):
            self.createHeap()
            self.L[0], self.L[self.size] = self.L[self.size], self.L[0]
            self.size -= 1
            print(self.L,self.size)
    
    def createHeap(self):
        for i in range((self.size-1)//2, -1, -1):
            self.heapify(i)
    
    def heapify(self,i):
        if 2*i+1<=self.size and self.L[2*i+1]>self.L[i]:
            largest = 2*i+1
        else:
            largest = i
        if 2*i+2<=self.size and self.L[2*i+2]>self.L[largest]:
            largest = 2*i+2
        if largest!=i:
            self.L[i], self.L[largest] = self.L[largest], self.L[i]
            self.heapify(largest)
            
            
heap3 = solution3([3,4,0,3,-1,99,0,2,5])
#heap3 = solution3([4,9,8])
print('original list:',heap3.L,'size:',heap3.size)
heap3.heapSort()
print('sorted list:',heap3.L)