import json
import random

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def test(request):
    return render(request, "viz/algorithm.html")


def bubble_sort(request):
    # Generate a random list of integers to sort
    original_list = [random.randint(1, 500) for _ in range(50)]

    # Perform bubble sort
    sorted_list = original_list.copy()
    steps = []
    for i in range(len(sorted_list) - 1):
        for j in range(len(sorted_list) - 1 - i):
            steps.append(sorted_list.copy())
            if sorted_list[j] > sorted_list[j + 1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]

    # Serialize the sorting steps as JSON data
    steps_json = json.dumps(steps)

    # Render the template with the sorted list and the sorting steps
    return render(
        request,
        "viz/algorithm.html",
        {
            "original_list": original_list,
            "sorted_list": sorted_list,
            "steps": steps_json,
        },
    )


def visualize_sort(request):

    # Convert the numbers to integers
    numbers = [1, 3, 5, 2, 7, 11, 4, 8]
    # Sort the numbers using the bubble sort algorithm
    # and generate a list of the intermediate states of the list
    sorted_numbers, intermediate_states = bubble_sort(numbers)
    print(sorted_numbers)
    # Render the visualization template and pass the sorted list and intermediate states to the template context
    return render(
        request,
        "viz/algorithm.html",
        {
            "sorted_numbers": sorted_numbers,
            "intermediate_states": intermediate_states,
        },
    )


def bubble_sortt(numbers):
    # Store the intermediate states of the list during the sorting process
    intermediate_states = []

    # Begin with the list in its original state
    intermediate_states.append(numbers[:])

    # Implement the bubble sort algorithm
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                # Swap the numbers
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

            # Store the intermediate state of the list
            intermediate_states.append(numbers[:])

    # Return the sorted list and the list of intermediate states
    return numbers, intermediate_states
