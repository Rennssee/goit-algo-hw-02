from collections import deque

def is_palindrome(input_string):
    # Перетворення рядку в нижній регістр та вилучення пробілів
    processed_string = input_string.lower().replace(" ", "")

    # Створення двосторонньої черги (deque)
    char_queue = deque(processed_string)

    # Порівняння символів з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False

    # Якщо дійшли до цього місця, рядок є паліндромом
    return True

# Користувач вводить рядок
user_input = input("Введіть рядок для перевірки на паліндром: ")

# Викликаємо функцію та виводимо результат
result = is_palindrome(user_input)

if result:
    print(f'"{user_input}" - це паліндром.')
else:
    print(f'"{user_input}" - не є паліндромом.')
