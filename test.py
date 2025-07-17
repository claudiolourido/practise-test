import pytest
from datetime import timedelta
from main import *


def test_format_time():
    assert format_time(timedelta(seconds=0)) == "0:00"
    assert format_time(timedelta(minutes=1, seconds=5)) == "1:05"
    assert format_time(timedelta(minutes=2, seconds=59)) == "2:59"

def test_schedule_task():
    t1 = schedule_task(timedelta(seconds=60), "Make sandwich")
    assert task_queue[-1] == (t1, "Make sandwich")
    assert t1 == timedelta(seconds=60)

    t2 = schedule_task(timedelta(seconds=90), "Serve sandwich")
    assert task_queue[-1] == (t2, "Serve sandwich")
    assert t2 == timedelta(seconds=150)  

def test_estimate_order_finish():
    t1 = estimate_order_finish()
    assert t1 == current_time + SANDWICH_MAKE_TIME + SANDWICH_SERVE_TIME

    schedule_task(SANDWICH_MAKE_TIME, "Make sandwich")
    t2 = estimate_order_finish()
    assert t2 == task_queue[-1][0] + SANDWICH_MAKE_TIME + SANDWICH_SERVE_TIME



def test_full_order_process():
    global task_queue, current_time, sandwich_inventory

    task_queue = []
    current_time = timedelta(seconds=0)
    sandwich_inventory = 45

    results = [place_sandwich_order() for _ in range(44)]

    results.append(place_sandwich_order())

    results.append(place_sandwich_order())

    assert results[:-1] == ["accepted"] * 45
    assert results[-1] in ("rejected_wait", "rejected_inventory")

    assert len(task_queue) == 90

    assert task_queue[0][1] == "Make sandwich"
    assert task_queue[-1][1] == "Serve sandwich"
