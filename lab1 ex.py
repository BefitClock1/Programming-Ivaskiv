
def longest_peak(arr):
    if len(arr) < 3:
        print("There must be at least 3 numbers")
        return
    
    max_length = 0
    max_pit_length = 0  
    all_lengths = []
    peak_numbers = []  
    pit_numbers = []  
    n = len(arr)
    
    i = 1
    while i < n - 1:
        if arr[i - 1] < arr[i] > arr[i + 1]:
            left = i - 1
            while left > 0 and arr[left - 1] < arr[left]:
                left -= 1
            
            right = i + 1
            while right < n - 1 and arr[right] > arr[right + 1]:
                right += 1
            
            peak_length = right - left + 1
            max_length = max(max_length, peak_length)
            all_lengths.append(peak_length)
            peak_numbers.append(arr[left:right + 1])  
        
        if arr[i - 1] > arr[i] < arr[i + 1]:
            left_pit = i - 1
            while left_pit > 0 and arr[left_pit - 1] > arr[left_pit]:
                if left_pit > 0 and arr[left_pit - 1] > arr[left_pit]:
                    left_pit -= 1
                else:
                    break
            
            right_pit = i + 1
            while right_pit < n - 1 and arr[right_pit] < arr[right_pit + 1]:
                right_pit += 1
            
            max_pit_length = max(max_pit_length, right_pit - left_pit + 1)
            pit_numbers.append(arr[left_pit:right_pit + 1])  
        
        i += 1
    
    print(max_length, max_pit_length, all_lengths, peak_numbers, pit_numbers)


longest_peak([1, 3, 5, 4, 2, 8, 3, 7])
