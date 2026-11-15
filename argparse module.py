import argparse

parser = argparse.ArgumentParser(description="Demo CLI")

# Main arguments
parser.add_argument("--count", type=int, default=1)
parser.add_argument("filename")
parser.add_argument("num_int", type=int)
parser.add_argument("num_float", type=float)
parser.add_argument("--op", choices=["add", "sub", "mul"])
parser.add_argument("-v", action="store_true")

# Subparsers
sub = parser.add_subparsers(dest="cmd", required=True)
add = sub.add_parser("add")
add.add_argument("num1", type=int)
add.add_argument("num2", type=int)

args = parser.parse_args()
print(args)

import pyfiglet