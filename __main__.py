from argparse import ArgumentParser
from sys import argv
from re import compile
from processor import add_recipe, expand_recipe
from colorama.ansi import Fore
from colorama import init

init(convert=True)

recipeFormat = compile(r"^\s*(\d+\*[A-Za-z0-9_-]+)\s*:\s*(\d+\*[A-Za-z0-9_-]+)(?:\s*,\s*\d+\*[A-Za-z0-9_-]+)*\s*$")

parser = ArgumentParser(prog="resource counter", description="count resources", epilog="It's a good program, don't you agree? XD")

parser.add_argument("-e", "--expand", type=str)
parser.add_argument("-c", "--count", type=int, default=1)
parser.add_argument("-r", "--recipe", type=str, help="-r (<count>*<item>:<count>*<item>, <count>*<item>, ...)")
parser.add_argument("-mc", action="store_true")

argv = parser.parse_args(argv[1:])

if argv.recipe:
    if recipeFormat.fullmatch(argv.recipe):
        add_recipe(argv.recipe)
    else:
        raise ValueError("Invalid recipe format (<count>*<item>:<count>*<item>, <count>*<item>, ...)")

if argv.expand:
    print("")
    expanded = expand_recipe(argv.expand, argv.count)
    print(f"{Fore.YELLOW}{argv.count} {argv.expand}{Fore.RESET}")
    if argv.mc:
        print("\n".join(f"{Fore.CYAN}{k}: {v}{Fore.RESET} :: {Fore.GREEN}({v//64})stack and ({v%64}){Fore.RESET}" for k, v in expanded.items()))
    else:
        print("\n".join(
            f"{Fore.CYAN}{k}: {v}{Fore.RESET}" for k, v in expanded.items()))
