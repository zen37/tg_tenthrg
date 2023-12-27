import pytest

from main import find_total1, find_total2, find_total3, find_total4, are_all_numbers

# Define the parameterized values
param_values = [
    ([],0),
    ([1, 2, 3], 2),
    ([10, 20, 30, 40, 50], 30),
    ([80, 30, 30], 80),
    ([1, 2, 3, 4], -2),
    ([1.0, 2.0, 3.0, 4.0], -2.0),
    ([1.77777, 2, 3.1111], 2.88887),
]

@pytest.mark.parametrize("input_list, expected_result", param_values)
def test_find_total1(input_list, expected_result):
    print("test_find_total1")
    assert find_total1(input_list) == expected_result


@pytest.mark.parametrize("input_list, expected_result", param_values)
def test_find_total2(input_list, expected_result):
    assert find_total2(input_list) == expected_result

@pytest.mark.parametrize("input_list, expected_result", param_values)
def test_find_total3(input_list, expected_result):
    assert find_total3(input_list) == expected_result

@pytest.mark.parametrize("input_list, expected_result", param_values)
def test_find_total4(input_list, expected_result):
    assert find_total4(input_list) == expected_result

def test_are_all_numbers():
    # Test case 1: All elements are numbers
    assert are_all_numbers([1, 2, 3, 4, 5])

    # Test case 2: List is empty
    assert are_all_numbers([])

    # Test case 3: Some elements are not numbers
    assert not are_all_numbers([1, 'two', 3, 4, 5])

    # Test case 4: All elements are floats
    assert are_all_numbers([1.0, 2.5, 3.7])