def mm(alist):
    print(alist)
    return merge_sort(alist)


def merge_sort(arr):
    # Initialize an empty list to store the animations
    animations = []

    # This function merges two sorted arrays
    def merge(arr, start, mid, end):
        # Split the arrays into left and right halves
        left = arr[start : mid + 1]
        right = arr[mid + 1 : end + 1]

        # Initialize indices for the left and right halves
        i = 0
        j = 0
        # Initialize an index for the original array
        k = start
        # Merge the two halves
        while i < len(left) and j < len(right):
            # If the element in the left half is smaller, add it to the original array
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            # If the element in the right half is smaller, add it to the original array
            else:
                arr[k] = right[j]
                j += 1
            # Add a merge animation
            animations.append(["merge", [k, arr[k]]])
            # Increment the index for the original array
            k += 1

        # Add any remaining elements from the left side
        while i < len(left):
            arr[k] = left[i]
            i += 1
            # Add a merge animation
            animations.append(["merge", [k, arr[k]]])
            k += 1

        # Add any remaining elements from the right side
        while j < len(right):
            arr[k] = right[j]
            j += 1
            # Add a merge animation
            animations.append(["merge", [k, arr[k]]])
            k += 1

    # This function sorts an array using merge sort
    def sort(arr, start, end):
        # If the array has more than one element, split and sort the two halves
        if start < end:
            # Split the array
            mid = (start + end) // 2
            # Add a split animation
            animations.append(["split", [i for i in range(start, end + 1)]])
            # Recursively sort the two halves
            sort(arr, start, mid)
            sort(arr, mid + 1, end)
            # Merge the sorted halves
            merge(arr, start, mid, end)

    # Sort the entire array
    sort(arr, 0, len(arr) - 1)
    return animations
