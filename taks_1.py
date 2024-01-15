import queue
import time

# Створення черги заявок
request_queue = queue.Queue()

# Змінна для унікальних номерів заявок
request_counter = 1

# Функція для генерації нових заявок
def generate_request():
    global request_counter
    new_request = f"Request {request_counter}"
    request_queue.put(new_request)
    print(f"Generated new request: {new_request}")
    request_counter += 1

# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        processed_request = request_queue.get()
        print(f"Processing request: {processed_request}")
    else:
        print("Queue is empty. No requests to process.")

# Головний цикл програми
while True:
    generate_request()  # Генерувати нові заявки
    time.sleep(2)  # Затримка для імітації роботи програми з часовим інтервалом
    process_request()  # Обробляти заявки
    time.sleep(1)  # Затримка між обробкою заявок
