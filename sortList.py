def sort_numbers(numbers):
    """
    Sort a list of numeric numbers in ascending order.

    :param numbers: List of numeric values (int or float).
    :return: Sorted list of numbers.
    """
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All elements must be numeric (int or float)")
    return sorted(numbers)

def second_smallest(numbers):
    """
    Return the second smallest unique number from the list.

    :param numbers: List of numeric values.
    :return: Second smallest unique number.
    """
    unique_numbers = sorted(set(numbers))
    if len(unique_numbers) < 2:
        raise ValueError("List must contain at least two unique numbers")
    return unique_numbers[1]

if __name__ == "__main__":
    n = int(input("Enter the number of numeric values: "))
    numbers = []
    for i in range(n):
        num = float(input(f"Enter number {i+1}: "))
        numbers.append(num)
    sorted_list = sort_numbers(numbers)
    print("Sorted list:", sorted_list)
    try:
        print("Second smallest number:", second_smallest(numbers))
    except ValueError as e:
        print(e)