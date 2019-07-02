from django.shortcuts import render

# Create your views here.
from .tasks import get_data


def test_func(priority, task_name):
    get_data.apply_async(args=(task_name,), priotity=priority)
    return priority
