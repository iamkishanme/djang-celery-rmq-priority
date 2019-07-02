from celery import task, shared_task
from celery import group, chain
from test_proj.celery import app

import time


@app.task(queue='task_one')
def task_one(task_name):
    number = 1
    for i in range(0, 10):
        print(task_name)
        print("Task One " + str(number))
        number += 1
        time.sleep(5)
    return number


@app.task(queue='task_two')
def task_two(task_name):
    number = 1
    for i in range(0, 10):
        print(task_name)
        print("Task Two " + str(number))
        number += 1
        time.sleep(2)
    return number


@app.task()
def get_data(task_name):
    task_one.apply_async(args=(task_name,))
    task_two.apply_async(args=(task_name,))
    return task_name
