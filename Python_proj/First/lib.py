
from colorama import Fore, init

# runs once; autoreset=True removes the need to write Style.RESET_ALL every time
init(autoreset=True)


def green(text, end="\n"):
    print(Fore.GREEN + str(text), end=end)


def red(text, end="\n"):
    print(Fore.RED + str(text), end=end)


def yellow(text, end="\n"):
    print(Fore.YELLOW + str(text), end=end)
    