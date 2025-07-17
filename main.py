from datetime import timedelta

task_queue = []
current_time = timedelta(seconds=0)
sandwich_inventory = 45  

SANDWICH_MAKE_TIME = timedelta(minutes=1)
SANDWICH_SERVE_TIME = timedelta(seconds=30)
SANDWICH_WAIT_LIMIT = timedelta(minutes=5)

def format_time(t):
    minutes = t.seconds // 60
    seconds = t.seconds % 60
    return f"{minutes}:{seconds:02}"

def get_last_task_time():
    return task_queue[-1][0] if task_queue else current_time

def schedule_task(delay_from_now, description):
    start_time = get_last_task_time()
    task_time = start_time + delay_from_now
    task_queue.append((task_time, description))
    return task_time

def estimate_order_finish():
    start = get_last_task_time()
    return start + SANDWICH_MAKE_TIME + SANDWICH_SERVE_TIME

def place_sandwich_order():
    global sandwich_inventory

    if sandwich_inventory <= 0:
        print(f"{format_time(current_time)} - Rejected sandwich order: out of stock")
        return "rejected_inventory"

    ready_time = estimate_order_finish()
    wait_time = ready_time - current_time

    if wait_time > SANDWICH_WAIT_LIMIT:
        print(f"{format_time(current_time)} - Rejected sandwich order: wait time {wait_time}")
        return "rejected_wait"

    sandwich_inventory -= 1
    schedule_task(SANDWICH_MAKE_TIME, "Make sandwich")
    schedule_task(SANDWICH_MAKE_TIME + SANDWICH_SERVE_TIME, "Serve sandwich")
    print(f"{format_time(current_time)} - Accepted sandwich order (ready in {wait_time})")
    return "accepted"

def print_schedule():
    print("\nFinal Schedule:")
    for time, task in task_queue:
        print(f"{format_time(time)} - {task}")
    if task_queue:
        last = task_queue[-1][0]
        print(f"{format_time(last + timedelta(seconds=30))} - take a well earned break!")

if __name__ == "__main__":
    for i in range(50):
        result = place_sandwich_order()
        if result.startswith("rejected"):
            print(f"Order {i+1}: {result}")

    print_schedule()
