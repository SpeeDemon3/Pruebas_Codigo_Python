from name_function import get_formatted_name

print("Enter [q] at any time to quit")

while True:
    first = input("\nPlease give me a first name:")
    last = input("\nPlease give me a last name:")

    if first.lower() == 'q' or last.lower() == 'q':
        break
    else:
        formatted_name = get_formatted_name(first, last)
        print(f"\tNeatly formatted name: {formatted_name}.")
