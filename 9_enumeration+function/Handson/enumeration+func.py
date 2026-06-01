def print_items_with_index(items):
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")


def list_string_characters(word):
    return [(index, letter) for index, letter in enumerate(word, start=1)]


def get_even_numbers_with_index(numbers):
    even_list = []
    for index, value in enumerate(numbers):
        if value % 2 == 0:
            even_list.append((index, value))
    return even_list


def describe_students(names):
    return [f"Student {index}: {name}" for index, name in enumerate(names, start=1)]


def main():
    print("==== ENUMERATE EXAMPLES ====")

    fruits = ["Apple", "Banana", "Cherry", "Date"]
    for index, fruit in enumerate(fruits, start=1):
        print(f"{index}. {fruit}")

    word = "Python"
    for idx, letter in enumerate(word, start=1):
        print(f"Letter {idx}: {letter}")

    print("\n==== FUNCTION EXAMPLES WITH ENUMERATE ====")

    print("-- Using print_items_with_index() --")
    print_items_with_index(fruits)

    print("\n-- Using list_string_characters() --")
    for idx, letter in list_string_characters(word):
        print(f"Letter {idx}: {letter}")

    print("\n-- Using get_even_numbers_with_index() --")
    numbers = [5, 12, 7, 20, 33, 42]
    even_items = get_even_numbers_with_index(numbers)
    for index, value in even_items:
        print(f"Index {index} -> {value}")

    print("\n-- Using describe_students() --")
    students = ["Asha", "Rohan", "Mira", "Karan"]
    descriptions = describe_students(students)
    for line in descriptions:
        print(line)

