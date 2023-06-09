import time


def bubbleSortAnimations(arr):
    startTime = time.time()
    listLength = len(arr)
    animations = (
        []
    )  # List of each comparison and replace, next iteration is doubled if values are replaced

    for i in range(listLength):
        animations.append(["step", 0, 0, 0, 1])
        for j in range(0, listLength - i - 1):
            animations.append(
                ["compare", j, j + 1, "step", 2]
            )  # Add elements that are compared into animation list
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                animations.append(["swap", j, j + 1, "step", 3])
                # Add elements that are replaced into animation list
        animations.append(["sorted", list(range(listLength, listLength - 1 - i, -1))])

    endTme = time.time()
    sortTime = endTme - startTime
    print(f"Bubble sort time: {sortTime}")
    print(animations)
    return animations


def mergeSortAnimations(arr):
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
            animations.append(["step", 0, 0, 2])
            # If the element in the left half is smaller, add it to the original array
            if left[i] < right[j]:
                animations.append(["step", 0, 0, 3])
                arr[k] = left[i]
                i += 1
            # If the element in the right half is smaller, add it to the original array
            else:
                animations.append(["step", 0, 0, 4])
                arr[k] = right[j]
                j += 1
            # Add a merge animation
            animations.append(["merge", [k, arr[k]], "step", 5])
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
    def mergeSort(arr, start, end):
        # If the array has more than one element, split and sort the two halves
        if start < end:
            # Split the array
            mid = (start + end) // 2
            # Add a split animation
            animations.append(["split", [i for i in range(start, end + 1)], "step", 0])
            # Recursively sort the two halves
            mergeSort(arr, start, mid)
            mergeSort(arr, mid + 1, end)
            # Merge the sorted halves
            animations.append(["step", 0, 0, 1])
            merge(arr, start, mid, end)

    # Sort the entire array
    mergeSort(arr, 0, len(arr) - 1)
    return animations


def selectionSortAnimations(arr):
    animations = []
    for i in range(len(arr)):
        animations.append(["step", 0, 0, 0, 0])
        min_idx = i
        for j in range(i + 1, len(arr)):
            animations.append(["compare", j, min_idx, "step", 1])
            if arr[j] < arr[min_idx]:
                animations.append(["step", 0, 0, 0, 2])
                min_idx = j
        animations.append(["swap", i, min_idx, "step", 3])
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        animations.append(["sorted", [k for k in range(i + 1)]])
    return animations


def countingSort(array, place, animations):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        animations.append(["compare", i])
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        animations.append(["swap", count[index % 10] - 1, array[i]])
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSortAnimations(array):
    startTime = time.time()
    # Get maximum element
    max_element = max(array)
    animations = []
    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place, animations)
        place *= 10

    endTme = time.time()
    sortTime = endTme - startTime
    print(f"Radix sort time: {sortTime}")
    return animations


def quickSortAnimations(array):
    def partition(array, low, high, animations):

        # choose the rightmost element as pivot
        pivot = array[high]
        animations.append(["pivot", high])
        # pointer for greater element
        i = low - 1

        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            animations.append(["compare", j])
            if array[j] <= pivot:
                # If element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1

                # Swapping element at i with element at j
                (array[i], array[j]) = (array[j], array[i])
                animations.append(["swap", i, j])

        # Swap the pivot element with the greater element specified by i
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        animations.append(["swap", i + 1, high])
        # Return the position from where partition is done
        return i + 1

    # function to perform quicksort

    def quickSort(array, low, high, animations):
        if low < high:

            # Find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pivot = partition(array, low, high, animations)

            # Recursive call on the left of pivot
            quickSort(array, low, pivot - 1, animations)

            # Recursive call on the right of pivot
            quickSort(array, pivot + 1, high, animations)

    animations = []
    quickSort(array, 0, len(array) - 1, animations)

    return animations


def insertSortAnimations(arr):
    animations = []
    if (n := len(arr)) <= 1:
        return
    animations.append(["step", 0, 0, 0, 0])
    animations.append(["sorted", [0]])
    for i in range(1, n):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        animations.append(["key", i, "step", 0, 1])
        j = i - 1
        if j >= 0 and key >= arr[j]:
            animations.append(["step", 0, 0, 0, 3])
        while j >= 0 and key < arr[j]:
            animations.append(["compare", j, "step", 0, 2])
            animations.append(["swap", j + 1, j, "step", 4])
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        animations.append(["sorted", [k for k in range(i + 1)]])

    print(animations)
    return animations
