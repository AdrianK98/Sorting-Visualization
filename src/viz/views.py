import json
import random

from celery.result import AsyncResult
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from viz.tasks import getAnimationsTask

from .methods import Method
from .models import Values
from .sortMethodHandler import SortMethodHandler


# Send requests from ajax to check if task is done
def checkStatus(request):
    task_id = request.GET.get("task_id")
    task = AsyncResult(task_id)
    data = {"status": task.status}
    return JsonResponse(data, status=200)


# Send to frontend task results
def getResult(request):
    task_id = request.GET.get("task_id")
    task = AsyncResult(task_id)
    data = {"result": task.result}
    return JsonResponse(data, status=200)


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


# Generate list of random values
def getValueList(size):
    randomGeneratedValues = [
        random.randint(10, 300) for _ in range(size)
    ]  # Generate a random list of integers to sort
    return randomGeneratedValues


def startingPage(request):

    # if request.method == "POST":
    #     arraySize = request.POST.get("slider_value")

        # Create model of Values if user has selected array size
    values = Values()
    randomListOfValues = getValueList(int(11))

    # Serialize values
    values.valueList = json.dumps(randomListOfValues)
    values.save()
    return render(request, "viz/startPage.html", {"values": values,"pageName": "start"})
    # return render(request, "viz/startPage.html", {})


# ONLY FOR TESTING
def testing(request, pk):
    # Set json decoder
    jsonDec = json.decoder.JSONDecoder()

    # Retrive from database list of values based on its id
    values = Values.objects.get(id=pk)

    # Decode
    originalArr = jsonDec.decode(values.valueList)

    arr = originalArr.copy()
    task = getAnimationsTask.apply_async(args=["bubbleSort", arr])
    return render(
        request,
        "viz/testing.html",
        {"task_id": task.id, "valueList": originalArr},
    )


def bubbleSort(request, pk):
    # Set json decoder
    jsonDec = json.decoder.JSONDecoder()

    # Retrive from database list of values based on its id
    values = Values.objects.get(id=pk)

    # Decode
    originalArr = jsonDec.decode(values.valueList)

    arr = originalArr.copy()

    # Start sorting and creating animation list task to workers
    task = getAnimationsTask.apply_async(args=["bubbleSort", arr])

    return render(
        request,
        "viz/bubble.html",
        {"task_id": task.id, "valueList": originalArr, "values": values},
    )


def insertSort(request, pk):
    # Set json decoder
    jsonDec = json.decoder.JSONDecoder()

    # Retrive from database list of values based on its id
    values = Values.objects.get(id=pk)

    # Decode
    originalArr = jsonDec.decode(values.valueList)

    arr = originalArr.copy()

    # Start sorting and creating animation list task to workers
    task = getAnimationsTask.apply_async(args=["insertSort", arr])

    return render(
        request,
        "viz/insert.html",
        {"task_id": task.id, "valueList": originalArr, "values": values},
    )


def mergeSort(request, pk):
    jsonDec = json.decoder.JSONDecoder()
    values = Values.objects.get(id=pk)
    originalArr = jsonDec.decode(values.valueList)

    arr = originalArr.copy()

    task = getAnimationsTask.apply_async(args=["mergeSort", arr])

    return render(
        request,
        "viz/merge.html",
        {"task_id": task.id, "valueList": originalArr, "values": values},
    )


def selectionSort(request, pk):
    jsonDec = json.decoder.JSONDecoder()
    values = Values.objects.get(id=pk)
    originalArr = jsonDec.decode(values.valueList)

    arr = originalArr.copy()

    # Get selection sort animations
    task = getAnimationsTask.apply_async(args=["selectionSort", arr])

    return render(
        request,
        "viz/selection.html",
        {"task_id": task.id, "valueList": originalArr, "values": values},
    )


def radixSort(request, pk):
    jsonDec = json.decoder.JSONDecoder()
    values = Values.objects.get(id=pk)
    originalArr = jsonDec.decode(values.valueList)

    arr = originalArr.copy()

    # Get selection sort animations
    task = getAnimationsTask.apply_async(args=["radixSort", arr])

    return render(
        request,
        "viz/radix.html",
        {"task_id": task.id, "valueList": originalArr, "values": values},
    )


def quickSort(request, pk):
    jsonDec = json.decoder.JSONDecoder()
    values = Values.objects.get(id=pk)
    originalArr = jsonDec.decode(values.valueList)

    arr = originalArr.copy()

    # Get selection sort animations
    task = getAnimationsTask.apply_async(args=["quickSort", arr])

    return render(
        request,
        "viz/quick.html",
        {"task_id": task.id, "valueList": originalArr, "values": values},
    )
