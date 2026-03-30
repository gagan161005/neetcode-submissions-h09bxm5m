class Solution:
    def replaceElements(self, arr):
        maxs =-1
        for i in range(len(arr)-1,-1,-1):
            curr =arr[i]
            arr[i]=maxs
            maxs =max(curr,maxs)
        return arr