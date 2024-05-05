import Lab2
import pytest
print("Test_Lab2")


def test_bubble_sort_find_min_max():
    int_list = [1,2,3]
    result = Lab2.calc_min_and_max_temp(int_list)
    assert (result == (1,3))


def test_bubble_sort_calc_average():
    int_list = [1,2,3]
    result = Lab2.calc_average_temp(int_list)
    assert (result == 2)


def test_bubble_sort_calc_median_temperature():
    int_list = [1,2,3]
    result = Lab2.calc_median_temperature(int_list)
    assert (result == 2)

    
