import time

from celery import shared_task

from .sort import bubbleSortAnimations


@shared_task
def bubbleTask(array):
    return bubbleSortAnimations(array)


@shared_task
def testTask(array):
    time.sleep(5)
    return bubbleSortAnimations(array)
