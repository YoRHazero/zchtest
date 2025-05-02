"""A simple CLI application that greets the user."""
import argparse
def hello():
    """A simple hello world function."""
    parser = argparse.ArgumentParser(description="Hello World CLI")
    parser.add_argument(
        "--name",
        type=str,
        default="World",
        help="Name to greet (default: World)",
    )
    args = parser.parse_args()
    print(f"Hello, {args.name}!")
    
    