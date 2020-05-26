import argparse

parser = argparse.ArgumentParser(description="")

parser.add_argument("--add", help="Add a new item to my ToDo List", type=str, nargs="+")
parser.add_argument("--remove", help="Remove item from my ToDo List", type=int)
parser.add_argument("--done", help="Mark the item as done from my ToDo List", type=int)
parser.add_argument("--undone", help="Mark item as not done from my ToDo List", type=int)
parser.add_argument("--view", help="View the ToDo list or view a specific item from ToDo List", type=int, nargs="*")
parser.add_argument("--description", help="Add description to a ToDo item", nargs="*")
parser.add_argument("--due", help="Add due date for an ToDo item", nargs="*")
