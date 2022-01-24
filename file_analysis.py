"""
This module represents tools of file analyzing.
You can run it from command line or import it as a module.
"""

import typing
import argparse
import string

parser = argparse.ArgumentParser(
    prog="Proceess a file", description="Analyze a given file data"
)
parser.add_argument("f", type=str, nargs="*", help="File name")
parser.add_argument("-L", action="store_true", help="Return the longest line")
parser.add_argument("-W", action="store_true", help="Return the longest word")
parser.add_argument("-a", action="store_true", help="Return all characteristics")
args = parser.parse_args()

MODE = typing.Literal["L", "W", "a"]


def analysis(file: str = args.f, mode: MODE = False) -> None:
    """
    The function analyzes what and how many a given file contains

    Args:
        file (str): The file is a file name or a file path
        mode (str): The mode determines what information needs to be returned:
                    L - Print longest lines
                    W - Print longest words
                    a - Print a number of lines including punctuation symbols,
                        words and characters excluding punctuation symbols

    Returns:
        None
    """
    if isinstance(file, list):
        file = file[0]
    lines = []
    with open(file, encoding="utf-8") as input_file:
        for line in input_file:
            lines.append(line.strip())

    args_t = (args.L, args.W, args.a)

    if (all(args_t) or not any(args_t)) and not mode:
        print(
            f"\nThere are {count_lines(lines)} lines,",
            f"{count_words(lines)} words,",
            f"{count_chars(lines)} characters in the file.\n",
        )

        print("The longest lines:")
        for line in the_longest_lines(lines):
            print(f"\t\t  {line!r}\n")

        print("The longest words:")
        for word in the_longest_words(lines):
            print(f"\t\t  {word!r}")

    elif args.L or mode == "L":
        print("The longest lines:")
        for line in the_longest_lines(lines):
            print(f"\t\t  {line!r}\n")

    elif args.W or mode == "W":
        print("The longest words:")
        for word in the_longest_words(lines):
            print(f"\t\t  {word!r}")

    else:
        print(
            f"There are {count_lines(lines)} lines,",
            f"{count_words(lines)} words,",
            f"{count_chars(lines)} characters in the file.",
        )


def the_longest_lines(lines: typing.List[str]) -> typing.Set[str]:
    """
    The function figures out the longest lines including punctuation symbols

    Args:
        lines (List[str]): The lines is a list of lines

    Returns:
        Set[str]: The function returns a set of the longest lines
    """
    longest = max(lines, key=len)

    return {line.rstrip() for line in [i for i in lines if len(i) == len(longest)]}


def the_longest_words(lines: typing.List[str]) -> typing.Set[str]:
    """
    The function figures out the longest words

    Args:
        lines (List[str]): The lines is a list of lines

    Returns:
        Set[str]: The function returns a set of the longest words
    """
    longest = max(
        [j.strip(string.punctuation) for i in lines for j in i.split()], key=len
    )

    return set(
        [
            j.strip(string.punctuation)
            for i in lines
            for j in i.split()
            if len(j.strip(string.punctuation)) == len(longest)
        ]
    )


def count_lines(lines: typing.List[str]) -> int:
    """
    The function figures out a number of lines

    Args:
        lines (List[str]): The lines is a list of lines

    Returns:
        Int: The function returns a number of lines
    """
    return len(lines)


def count_words(lines: typing.List[str]) -> int:
    """
    The function figures out a number of words

    Args:
        lines (List[str]): The lines is a list of lines

    Returns:
        Int: The function returns a number of words
    """
    return len([j for i in lines for j in i.split()])


def count_chars(lines: typing.List[str]) -> int:
    """
    The function figures out a number of characters excluding punctuation symbols

    Args:
        lines (List[str]): The lines is a list of lines

    Returns:
        Int: The function returns a number of characters
    """

    return len([j.strip(string.punctuation) for i in lines for j in i if j != " "])


if __name__ == "__main__":
    analysis()
else:
    print("file_analysis loaded as a module")
