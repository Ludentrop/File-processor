import typing, argparse, string

parser = argparse.ArgumentParser(
    prog="word_frxy", description="Find the most popular and unpopular words"
)
parser.add_argument("f", type=str, nargs="*", help="File name")
parser.add_argument("-m", action="store_true", help="Return the most frequent words")
parser.add_argument("-l", action="store_true", help="Return less frequent words")

args = parser.parse_args()
args_t = (args.m, args.l)
MODE = typing.Literal["m", "l"]


def main(file: str = args.f, mode: MODE = False) -> None:
    """
    The function print the most frequent and less frequent words

    Args:
        file (str): The file is a file name or a file path
        mode (str): The mode determines what information needs to be returned:
                    m - Print the most frequent words
                    l - Print less frequent words
    Returns:
        None
    """
    lines = get_from_file(args.f)
    normalized = normalize(lines)
    frxy_dict = word_frxy(normalized)

    if not bool(frxy_dict):
        print("All words are unique")
    else:
        if (all(args_t) or not any(args_t)) and not mode:
            print("THE MOST FREQUENT WORDS:")
            for word in m(frxy_dict):
                print(f"\t\t\t{word!r}")

            print("\nLESS FREQUENT WORDS:")
            for word in l(frxy_dict):
                print(f"\t\t\t{word!r}")

        elif args.m:
            print("THE MOST FREQUENT WORDS:")
            for word in m(frxy_dict):
                print(f"\t\t  {word!r}")

        elif args.l:
            print("LESS FREQUENT WORDS:")
            for word in l(frxy_dict):
                print(f"\t\t  {word!r}")


def get_from_file(file: str) -> typing.List[str]:
    """
    The function extracts lines from a given file

    Args:
        file (str): The file is a file name or a file path

    Returns:
        List[str]: A list of lines
    """
    if isinstance(file, list):
        file = file[0]
    lines = [line.strip() for line in open(file, encoding="utf-8")]

    return lines


def normalize(lines: typing.List[str]) -> typing.List[str]:
    """
    The function normalizes given lines of a list

    Args:
        lines (typing.List[str]): The lines is a list of lines

    Returns:
        List[str]: A list of words
    """
    return [j.strip(string.punctuation) for i in lines for j in i.split()]


def word_frxy(lines: typing.List[str]) -> typing.Dict[str, int]:
    """
    The function determines each word frequency

    Args:
        lines (List[str]): The lines is a list of words

    Returns:
        words (Dict[str, int]): A dictionary of pairs "word: frequency"
    """
    if len(set(lines)) == len(lines):
        return ""
    else:
        words = {}
        for line in lines:
            words[line] = words.get(line, 0) + 1

        return words


def m(dct: typing.Dict[str, int]) -> typing.List[str]:
    """
    The function finds the most popular words

    Args:
        dct (Dict[str, int]): The dict is a dictionary of pairs "word: frequency"

    Returns:
        typing.List[str]: A list of the most popular words
    """
    mx = max(dct.values())
    return [k for k in dct.keys() if dct[k] == mx]


def l(dct: typing.Dict[str, int]) -> typing.List[str]:
    """
    The function finds unpopular words

    Args:
        dct (Dict[str, int]): The dict is a dictionary of pairs "word: frequency"

    Returns:
        typing.List[str]: A list of unpopular words
    """
    mn = min(dct.values())
    return [k for k in dct.keys() if dct[k] == mn]


if __name__ == "__main__":
    main()
else:
    print("word_frxy loaded as a module")
