def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Test cases
test_case_1 = [12, 11, 13, 5, 6, 7]
test_case_2 = [38, 27, 43, 3, 9, 82, 10]
test_case_3 = [1, 20, 6, 4, 5]

print("Test Case 1:", merge_sort(test_case_1.copy()))  # Output should be [5, 6, 7, 11, 12, 13]
print("Test Case 2:", merge_sort(test_case_2.copy()))  # Output should be [3, 9, 10, 27, 38, 43, 82]
print("Test Case 3:", merge_sort(test_case_3.copy()))  # Output should be [1, 4, 5, 6, 20]
