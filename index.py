# Python code to add two numbers
import sys
import os
import subprocess

def add_numbers(a: int | float, b: int | float) -> int | float:
    if type(a) not in (int, float):
        raise TypeError(f"Expected int or float for 'a', got {type(a).__name__}")
    if type(b) not in (int, float):
        raise TypeError(f"Expected int or float for 'b', got {type(b).__name__}")
    return a + b

def main() -> None:
    try:
        # Core logic
        result = add_numbers(5, 10)
        print(f"The sum is: {result}")
        
        # ----------------─────────────────────────────────────────
        # ISSUE 1: Path Traversal (Low/Medium)
        # ----------------─────────────────────────────────────────
        # Source: Command line position 1
        if len(sys.argv) > 1:
            file_path_input = sys.argv[1] 
            with open(file_path_input, 'r') as user_file:
                print(user_file.read())

        # ----------------─────────────────────────────────────────
        # ISSUE 2: High-Severity Command Injection (High)
        # ----------------─────────────────────────────────────────
        # Source: Command line position 2 (Guarantees active input tracking)
        if len(sys.argv) > 2:
            cmd_injection_input = sys.argv[2]
            # shell=True combined with an active shell argument forces a HIGH rule match
            subprocess.check_call(f"ping -c 1 {cmd_injection_input}", shell=True)

    except TypeError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
