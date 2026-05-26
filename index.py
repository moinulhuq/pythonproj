# Python code to add two numbers
import sys
import os
import subprocess

# ---------------------------------------------------------
# ISSUE 3: Hardcoded Secret (High Severity)
# ---------------------------------------------------------
API_KEY = "12345-SECRET-KEY"   # Aikido will flag this as a secret leak

def add_numbers(a: int | float, b: int | float) -> int | float:
    if type(a) not in (int, float):
        raise TypeError(f"Expected int or float for 'a', got {type(a).__name__}")
    if type(b) not in (int, float):
        raise TypeError(f"Expected int or float for 'b', got {type(b).__name__}")
    return a + b

def subtract_numbers(a: int | float, b: int | float) -> int | float:
    if type(a) not in (int, float):
        raise TypeError(
            f"Expected int or float for 'a', got {type(a).__name__}"
        )
    if type(b) not in (int, float):
        raise TypeError(
            f"Expected int or float for 'b', got {type(b).__name__}"
        )
    return a - b

def main() -> None:
    try:
        # Core logic
        result = add_numbers(5, 10)
        print(f"The sum is: {result}")
        
        # ---------------------------------------------------------
        # ISSUE 1: Path Traversal (Medium Severity)
        # ---------------------------------------------------------
        # Using user-supplied path directly
        if len(sys.argv) > 1:
            file_path_input = sys.argv[1]
            with open(file_path_input, 'r') as user_file:
                print(user_file.read())

        # ---------------------------------------------------------
        # ISSUE 2: Command Injection (High Severity)
        # ---------------------------------------------------------
        if len(sys.argv) > 2:
            cmd_injection_input = sys.argv[2]
            # Strongest pattern: concatenation + shell=True
            vulnerable_cmd = "ping -c 1 " + cmd_injection_input
            subprocess.check_call(vulnerable_cmd, shell=True)

    except TypeError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

    try:
        result = subtract_numbers(5, 10)
        print(f"The difference is: {result}")
    except TypeError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

