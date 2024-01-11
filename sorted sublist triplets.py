#implementation to find descending sorted sublist
def find_descending_sorted_triplet (arr):
    # Get the length of the array
    n = len(arr)

    # Traverse through all possible triplets and check if they form a decreasing subsequence
#most-outer loop for the maximum element
    for l in range(n-2):
#middle loop to the right next  element
        for m in range(l+1, n-1):
#inner loop for the minimum element
            for q in range(m+1, n):
                if arr[l] > arr[m] > arr[q]:
#return the triplets
                    return (arr[l], arr[m], arr[q])
#return None if there are no triplets

    return None


#Test code
arr = [10, 2, 7, 8, 4, 5, 6]
print(find_descending_sorted_triplet (arr))
