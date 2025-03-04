# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-04-06 13:50:23
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2024-04-06 20:11:00

"""
Test calculator using pytest
"""
from enum import Enum
from typing import List, Tuple
from unittest.mock import patch

import pytest

from main import calculate, get_operator, main


class Message(Enum):
    """
    Message class
    """

    WELCOME = "Welcome to the Python calculator!"
    ANSWER = "The answer is {answer}"
    REMAINDER = "The remainder is {remainder}"


class TstCase(Enum):
    """
    TestCase class
    """

    OPERATIONS = (
        ("3+5",),
        ("3-5",),
        ("3*5",),
        ("3/5",),
        ("3~5",),
        ("15+3",),
        ("5*13",),
        ("15~13",),
    )
    MAIN = (
        (1, "3+5"),
        (1, "3-5"),
        (1, "3*5"),
        (1, "3/5"),
        (1, "3~5"),
        (2, "3+5", "3-5"),
        (1, "15+3"),
        (1, "5*13"),
        (1, "15~13"),
    )


@pytest.fixture(params=TstCase.OPERATIONS.value, name="get_operator_io")
def get_operator_fixture(request) -> Tuple[str, str]:
    """
    Returns tuple of operation and expected operator found by the function get_operator
    """
    operation = request.param[0]
    if operation == "3+5":
        expected_operator = "+"
    if operation == "3-5":
        expected_operator = "-"
    if operation == "3*5":
        expected_operator = "*"
    if operation == "3/5":
        expected_operator = "/"
    if operation == "3~5":
        expected_operator = "~"
    if operation == "15+3":
        expected_operator = "+"
    if operation == "5*13":
        expected_operator = "*"
    if operation == "15~13":
        expected_operator = "~"

    return operation, expected_operator


@pytest.fixture(params=TstCase.OPERATIONS.value, name="calculate_io")
def calculate_fixture(request) -> Tuple[str, str]:
    """
    Returns tuple of operation and expected output of the function calculate
    """
    operation = request.param[0]
    if operation == "3+5":
        expected_output = Message.ANSWER.value.format(answer=8)
    if operation == "3-5":
        expected_output = Message.ANSWER.value.format(answer=-2)
    if operation == "3*5":
        expected_output = Message.ANSWER.value.format(answer=15)
    if operation == "3/5":
        expected_output = Message.ANSWER.value.format(answer=0.6)
    if operation == "3~5":
        expected_output = Message.ANSWER.value.format(answer=0)
        expected_output += "\n" + Message.REMAINDER.value.format(remainder=3)
    if operation == "15+3":
        expected_output = Message.ANSWER.value.format(answer=18)
    if operation == "5*13":
        expected_output = Message.ANSWER.value.format(answer=65)
    if operation == "15~13":
        expected_output = Message.ANSWER.value.format(answer=1)
        expected_output += "\n" + Message.REMAINDER.value.format(remainder=2)

    return operation, expected_output


@pytest.fixture(params=TstCase.MAIN.value, name="main_io")
def main_fixture(request) -> Tuple[int, List[str], str]:
    """
    Returns tuple of number of operations, list of operations and expected output
    of the function main
    """
    expected_output = Message.WELCOME.value
    nb_operations, *operations = request.param

    if request.param == (1, "3+5"):
        expected_output += "\n" + Message.ANSWER.value.format(answer=8)
    if request.param == (1, "3-5"):
        expected_output += "\n" + Message.ANSWER.value.format(answer=-2)
    if request.param == (1, "3*5"):
        expected_output += "\n" + Message.ANSWER.value.format(answer=15)
    if request.param == (1, "3/5"):
        expected_output += "\n" + Message.ANSWER.value.format(answer=0.6)
    if request.param == (1, "3~5"):
        expected_output += "\n" + Message.ANSWER.value.format(answer=0)
        expected_output += "\n" + Message.REMAINDER.value.format(remainder=3)
    if request.param == (2, "3+5", "3-5"):
        expected_output += "\n" + Message.ANSWER.value.format(answer=8)
        expected_output += "\n" + Message.ANSWER.value.format(answer=-2)
    if request.param == (1, "15+3"):
        expected_output += "\n" + Message.ANSWER.value.format(answer=18)
    if request.param == (1, "5*13"):
        expected_output += "\n" + Message.ANSWER.value.format(answer=65)
    if request.param == (1, "15~13"):
        expected_output += "\n" + Message.ANSWER.value.format(answer=1)
        expected_output += "\n" + Message.REMAINDER.value.format(remainder=2)

    return nb_operations, operations, expected_output


def test_get_operator(get_operator_io):
    """
    Test function get_operator
    """
    operation, expected = get_operator_io
    output = get_operator(operation)
    assert output == expected


def test_calculate(capsys, calculate_io):
    """
    Test function calculate
    """
    operation, expected = calculate_io
    calculate(operation)
    captured = capsys.readouterr()
    output = captured.out.strip()
    assert output == expected


def test_main(capsys, main_io):
    """
    Test function main
    """
    nb_operations, operations, expected = main_io
    side_effect = operations.copy()
    side_effect.insert(0, nb_operations)

    with patch("builtins.input", side_effect=side_effect):
        main()
        captured = capsys.readouterr()
        output = captured.out.strip()
        assert output == expected
