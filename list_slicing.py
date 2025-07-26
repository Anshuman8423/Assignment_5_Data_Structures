# list_slicing.py

def demonstrate_slicing():
    numbers = list(range(1, 11))
    first_five = numbers[:5]
    reversed_list = first_five[::-1]

    print(f"Original list: {numbers}")
    print(f"First five elements: {first_five}")
    print(f"Reversed list: {reversed_list}")

if __name__ == "__main__":
    demonstrate_slicing()
