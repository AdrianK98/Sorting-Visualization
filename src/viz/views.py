import json
import random

from celery.result import AsyncResult
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from viz.tasks import getAnimationsTask

from .methods import Method
from .sortMethodHandler import SortMethodHandler


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
        random.randint(10, 9999) for _ in range(100)
    ]  # Generate a random list of integers to sort
    return randomGeneratedValues


def testing(request):

    originalArr = getValueList()
    arr = originalArr.copy()

    task = getAnimationsTask.apply_async(args=["bubbleSort", arr])

    return render(
        request,
        "viz/testing.html",
        {"task_id": task.id, "valueList": originalArr},
    )


def bubbleSort(request):
    originalArr = getValueList()
    arr = originalArr.copy()

    task = getAnimationsTask.apply_async(args=["bubbleSort", arr])

    return render(
        request,
        "viz/bubble.html",
        {"task_id": task.id, "valueList": originalArr},
    )


def mergeSort(request):
    originalArr = getValueList()
    arr = originalArr.copy()

    task = getAnimationsTask.apply_async(args=["mergeSort", arr])

    return render(
        request,
        "viz/merge.html",
        {"task_id": task.id, "valueList": originalArr},
    )


def selectionSort(request):
    originalArr = getValueList()
    arr = originalArr.copy()

    # Get selection sort animations
    task = getAnimationsTask.apply_async(args=["selectionSort", arr])

    return render(
        request,
        "viz/selection.html",
        {"task_id": task.id, "valueList": originalArr},
    )


def radixSort(request):
    originalArr = getValueList()

    arr = originalArr.copy()

    # Get selection sort animations
    task = getAnimationsTask.apply_async(args=["radixSort", arr])

    return render(
        request,
        "viz/radix.html",
        {"task_id": task.id, "valueList": originalArr},
    )


def quickSort(request):
    originalArr = getValueList()

    arr = originalArr.copy()

    # Get selection sort animations
    task = getAnimationsTask.apply_async(args=["quickSort", arr])

    return render(
        request,
        "viz/quick.html",
        {"task_id": task.id, "valueList": originalArr},
    )
