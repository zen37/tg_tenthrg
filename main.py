from constants import MSG_NOT_ALL_NUMBERS, NUMBERS_LIST

def find_total1(numbers_list) :
    """
    Calculate the difference between the sum of elements at even indices
    and the sum of elements at odd indices in the given list.

    Parameters:
    - list of numbers

    Returns:
    - The difference between the sum of even-indexed elements and odd-indexed elements.
    """
    even_sum = 0
    odd_sum = 0

    for i in range(len(numbers_list)):
        if i % 2 == 0:
            even_sum = even_sum + numbers_list[i]
        else:
            odd_sum = odd_sum + numbers_list[i]

    return even_sum - odd_sum

def find_total2(numbers_list) :
    """
    Calculate the difference between the sum of elements at even indices
    and the sum of elements at odd indices in the given list.

    Parameters:
    - list of numbers.

    Returns:
    - difference between the sum of even-indexed elements and odd-indexed elements.
    """
    even_sum = 0
    odd_sum = 0

    for index, value in enumerate(numbers_list):
        if index % 2 == 0:
            even_sum += value
        else:
            odd_sum += value

    return even_sum - odd_sum

def find_total3(numbers_list):
    """
    Calculate the difference between the sum of elements at even indices
    and the sum of elements at odd indices in the given list.

    Parameters:
    - list of numbers.

    Returns:
    - difference between the sum of even-indexed elements and odd-indexed elements.
    """
    even_sum = sum(numbers_list[i] for i in range(0, len(numbers_list), 2))
    odd_sum = sum(numbers_list[i] for i in range(1, len(numbers_list), 2))

    return even_sum - odd_sum

def find_total4(numbers_list):
    """
    Calculate the difference between the sum of elements at even indices
    and the sum of elements at odd indices in the given list.

    Parameters:
    - list of numbers.

    Returns:
    - difference between the sum of even-indexed elements and odd-indexed elements.
    """
    even_sum = sum([numbers_list[i] for i in range(0, len(numbers_list), 2)])
    odd_sum = sum([numbers_list[i] for i in range(1, len(numbers_list), 2)])

    return even_sum - odd_sum

def are_all_numbers(input_list):
    return all(isinstance(item, (int, float)) for item in input_list)


def main():
    numbers_list = NUMBERS_LIST

    if not are_all_numbers(numbers_list):
        print(MSG_NOT_ALL_NUMBERS )
        return

    print("find_total1:", find_total1(numbers_list))
    print("find_total2:", find_total2(numbers_list))
    print("find_total3:", find_total3(numbers_list))
    print("find_total4:", find_total4(numbers_list))

if __name__ == "__main__":
    main()