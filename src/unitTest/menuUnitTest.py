import pytest

import src.menu as menu


def test_new_phone():
    # Override the Python built-in input method

    menu.input = input
    # Call the function you would like to test (which uses input)
    output = menu.createPhone()
    assert output == 'expected_output'