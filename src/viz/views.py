import json
import random
import time

from celery.result import AsyncResult
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from viz.tasks import bubbleTask, testTask

from .sort import *


def checkStatus(request):
    print("CHECKING STATUS")
    task_id = request.GET.get("task_id")
    task = AsyncResult(task_id)
    data = {"status": task.status}
    return JsonResponse(data, status=200)


def getResult(request):
    print("RETRIVING RESULTS")
    task_id = request.GET.get("task_id")
    task = AsyncResult(task_id)
    data = {"result": task.result}
    return JsonResponse(data, status=200)


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


def getValueList():
    randomGeneratedValues = [
        random.randint(10, 9999) for _ in range(30)
    ]  # Generate a random list of integers to sort
    return randomGeneratedValues


def testing(request):

    originalArr = getValueList()
    arr = originalArr.copy()
    task = testTask.apply_async(args=[arr])

    return render(
        request,
        "viz/testing.html",
        {"task_id": task.id, "valueList": originalArr},
    )


def bubbleSort(request):
    originalArr = getValueList()
    arr = originalArr.copy()
    task = testTask.apply_async(args=[arr])

    return render(
        request,
        "viz/bubble.html",
        {"task_id": task.id, "valueList": originalArr},
    )


def mergeSort(request):
    originalArr = getValueList()
    arr = originalArr.copy()

    # Get merge sort animations
    animations = mergeSortAnimations(arr)

    return render(
        request,
        "viz/merge.html",
        {"valueList": originalArr, "animations": json.dumps(animations)},
    )


def selectionSort(request):
    originalArr = getValueList()
    arr = originalArr.copy()

    # Get selection sort animations
    animations = selectionSortAnimations(arr)

    return render(
        request,
        "viz/selection.html",
        {"valueList": originalArr, "animations": json.dumps(animations)},
    )


def radixSort(request):
    originalArr = getValueList()

    arr = originalArr.copy()

    # Get selection sort animations
    animations = radixSortAnimations(arr)

    return render(
        request,
        "viz/radix.html",
        {"valueList": originalArr, "animations": json.dumps(animations)},
    )


def quickSort(request):
    originalArr = getValueList()

    arr = originalArr.copy()

    # Get selection sort animations
    animations = quickSortAnimations(arr)

    return render(
        request,
        "viz/quick.html",
        {"valueList": originalArr, "animations": json.dumps(animations)},
    )
