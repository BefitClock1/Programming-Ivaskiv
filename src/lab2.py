def sort(arr): #Вставка
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def can_place_cows(free_sections, C, min_dist):
    count = 1  
    last_position = free_sections[0]
    
    for i in range(1, len(free_sections)):
        if free_sections[i] - last_position >= min_dist:
            count += 1
            last_position = free_sections[i]
            if count == C:
                return True
    
    return False

def largest_min_distance(N, C, free_sections):
    sort(free_sections)  
    low = 1
    high = free_sections[-1] - free_sections[0]
    best = 0
    
    while low <= high:
        mid = (low + high) // 2
        if can_place_cows(free_sections, C, mid):
            best = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return best
