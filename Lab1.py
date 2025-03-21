import unittest

def longest_peak(arr):
    if len(arr) < 3:
        return "There must be more than 3 numbers"
    
    max_length = 0
    n = len(arr)
    
    i = 1
    while i < n - 1 :
        if arr[i - 1] < arr[i] > arr[i + 1]:
            left = i - 1
            while left >= 0 and arr[left - 1] < arr[left]:
                left -= 1
            
            right = i + 1
            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1
            
            max_length = max(max_length, right - left + 1)
        
        i += 1

    return max_length



arr = [1, 3, 5, 4, 2, 8, 3, 7]
print(longest_peak(arr))  


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
arr2 = [9, 8, 7, 6, 5, 4, 3, 2, 1] 
arr3 = [1, 2]  
arr4 = [1, 1, 1, 1, 1, 1, 1, 1]  
arr5 = [1, 3, 5, 4, 2, 6, 7, 8, 9, 8, 7, 6, 2, 8, 10, 6, 3]  

print(longest_peak(arr1))  
print(longest_peak(arr2))  
print(longest_peak(arr3))  
print(longest_peak(arr4))  
print(longest_peak(arr5))  

