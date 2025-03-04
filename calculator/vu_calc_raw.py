# -*- coding: utf-8 -*-
# @Author: VU Anh Tuan
# @Date:   2024-04-06 17:58:42
# @Last Modified by:   VU Anh Tuan
# @Last Modified time: 2024-04-07 08:35:47

"""
Test calculator by giving command to run script
"""

import subprocess
import sys
from enum import Enum
from pathlib import Path
from typing import Sequence

from colorama import Fore, Style, init
from tabulate import tabulate


class Message(Enum):
    """
    Message class
    """

    ANSWER = "The answer is"
    REMAINDER = "The remainder is"


def get_response(line: str) -> str:
    """
    Returns response from given line of stdout
    """
    for msg in Message:
        idx = line.find(msg.value)
        if idx > -1:
            return line[idx:]
    return ""


def run_command(command: str, user_inputs: Sequence) -> str:
    """
    Returns responses of given command and inputs
    """
    args = command.split()

    # check number of components
    if len(args) != 2:
        print(
            f"{Fore.RED}Expected a command of 2 componenets, got "
            f"{Style.BRIGHT}{len(args)}{Style.NORMAL}{Fore.RESET}."
        )
        sys.exit()

    # check script existence
    script_path = Path(args[-1])
    if not script_path.is_file():
        print(
            f"{Fore.RED}Not found script {Style.BRIGHT}"
            f"{script_path.name}{Style.NORMAL}{Fore.RESET}."
        )
        sys.exit()

    try:
        with subprocess.Popen(
            args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        ) as process:
            stdout, _ = process.communicate("\n".join(map(str, user_inputs)))
    except Exception as error:  # pylint: disable=broad-exception-caught
        print(f"{Fore.RED}{error}{Fore.RESET}.")
        sys.exit()

    responses = []
    for line in stdout.strip().split("\n"):
        response = get_response(line)
        if not response:
            continue
        responses.append(response)
    return "\n".join(responses)


def main():
    """
    Main function
    """
    init()  # initialise colorama

    # get command input
    command = input(f"{Style.BRIGHT}command: ")
    print(Style.NORMAL)

    # get results of test cases
    results = []
    for test_case in TEST_CASES:
        output = run_command(command, test_case)
        expected = get_expected_output(test_case)
        color = Fore.GREEN if output == expected else Fore.RED
        result = "PASSED" if output == expected else "FAILED"
        str_test_case = ", ".join(map(str, test_case))
        results.append([str_test_case, f"{color}{result}{Fore.RESET}"])

    # create table to print
    headers = [
        f"{Style.BRIGHT}Index{Style.NORMAL}",
        f"{Style.BRIGHT}Test Case{Style.NORMAL}",
        f"{Style.BRIGHT}Result{Style.NORMAL}",
    ]
    table = tabulate(
        results, headers=headers, showindex="always", tablefmt="rounded_outline"
    )
    print(table)


# DEFINE test cases and expected output
TEST_CASES = (
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


def get_expected_output(test_case: Sequence) -> str:
    """
    Returns expected output of test cases
    """
    expected_output = ""
    if test_case == (1, "3+5"):
        expected_output = f"{Message.ANSWER.value} 8"
    if test_case == (1, "3-5"):
        expected_output = f"{Message.ANSWER.value} -2"
    if test_case == (1, "3*5"):
        expected_output = f"{Message.ANSWER.value} 15"
    if test_case == (1, "3/5"):
        expected_output = f"{Message.ANSWER.value} 0.6"
    if test_case == (1, "3~5"):
        expected_output = "\n".join(
            [
                f"{Message.ANSWER.value} 0",
                f"{Message.REMAINDER.value} 3",
            ]
        )
    if test_case == (2, "3+5", "3-5"):
        expected_output = "\n".join(
            [
                f"{Message.ANSWER.value} 8",
                f"{Message.ANSWER.value} -2",
            ]
        )
    if test_case == (1, "15+3"):
        expected_output = f"{Message.ANSWER.value} 18"
    if test_case == (1, "5*13"):
        expected_output = f"{Message.ANSWER.value} 65"
    if test_case == (1, "15~13"):
        expected_output = "\n".join(
            [
                f"{Message.ANSWER.value} 1",
                f"{Message.REMAINDER.value} 2",
            ]
        )
    return expected_output


if __name__ == "__main__":
    main()
