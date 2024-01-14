from queue import Queue
from uuid import uuid4


queue = Queue()


def get_id() -> int:
    return str(uuid4())


def generate_request():
    request = {"id": get_id()}
    queue.put(request)
    print(f"Request with id: {request['id']} is successfully added to Queue")


def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Request with id: {request['id']} is processed")
    else:
        print("Queue is empty")


while True:
    try:
        generate_request()
        process_request()

    except KeyboardInterrupt:
        print("Program terminated by user.")
        break
