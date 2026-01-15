def mergeSort(nums):
        n = len(nums)
        for i in range(n):
            for j in range(0, n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        print(nums)  
      

mergeSort([38,27,43,3,9,82,10])
