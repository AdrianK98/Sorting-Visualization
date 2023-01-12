import json
import random

from django.http import HttpResponse
from django.shortcuts import render

from .sort import mergeSortAnimations, selectionSortAnimations


def test(request):
    return render(request, "viz/algorithm.html")


def bubbleSort(request):
    originalArr = [
        random.randint(1, 30) for _ in range(30)
    ]  # Generate a random list of integers to sort
    arr = originalArr.copy()
    listLength = len(arr)
    animations = (
        []
    )  # List of each comparison and replace, next iteration is doubled if values are replaced

    for i in range(listLength):
        for j in range(0, listLength - i - 1):
            animations.append(
                [j, j + 1]
            )  # Add elements that are compared into animation list
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                animations.append(
                    [j, j + 1]
                )  # Add elements that are replaced into animation list

    return render(
        request,
        "viz/bubble.html",
        {"animations": animations, "valueList": originalArr},
    )


def mergeSort(request):
    originalArr = [
        random.randint(1, 30) for _ in range(30)
    ]  # Generate a random list of integers to sort

    arr = originalArr.copy()

    # Get merge sort animations
    animations = mergeSortAnimations(arr)

    print(animations)
    return render(
        request,
        "viz/merge.html",
        {"valueList": originalArr, "animations": json.dumps(animations)},
    )


def selectionSort(request):
    originalArr = [
        random.randint(1, 30) for _ in range(30)
    ]  # Generate a random list of integers to sort

    arr = originalArr.copy()

    # Get selection sort animations
    animations = selectionSortAnimations(arr)
    print(originalArr)
    print(animations)
    return render(
        request,
        "viz/selection.html",
        {"valueList": originalArr, "animations": json.dumps(animations)},
    )
