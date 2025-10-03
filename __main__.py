from argparse import ArgumentParser
from sys import argv
from re import compile
from processor import add_recipe, expand_recipe

recipeFormat = compile(r"^\s*(\d+\*[A-Za-z0-9_-]+)\s*:\s*(\d+\*[A-Za-z0-9_-]+)(?:\s*,\s*\d+\*[A-Za-z0-9_-]+)*\s*$")

parser = ArgumentParser(prog="resource counter", description="count resources", epilog="It's a good program, don't you agree? XD")

parser.add_argument("-e", "--expand", type=str)
parser.add_argument("-c", "--count", type=int, default=1)
parser.add_argument("-r", "-recipe", type=str, help="-r (<count>*<item>:<count>*<item>, <count>*<item>, ...)")

argv = parser.parse_args(argv[1:])

if argv.r:
    if recipeFormat.fullmatch(argv.r):
        add_recipe(argv.r)
    else:
        raise ValueError("Invalid recipe format (<count>*<item>:<count>*<item>, <count>*<item>, ...)")

if argv.expand:
    expanded = expand_recipe(argv.expand, argv.count)
    print(f"{argv.count} {argv.expand}")
    print("\n".join(f"{k}  {v}" for k, v in expanded.items()))
