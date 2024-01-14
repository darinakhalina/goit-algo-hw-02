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
    user_input = input("Press 'Enter' to continue or 'q' to quit: ")

    if user_input.lower() == "q":
        print("Program completed.")
        break

    generate_request()
    process_request()
