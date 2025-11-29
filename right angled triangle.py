#!/usr/bin/env python3
def print_right_angled_triangle(height: int, align: str = "left") -> None:
    """
    Print a right-angled triangle of '*' of given height.
    align: "left" (default) or "right"
    """
    if height <= 0:
        return
    align = align.lower()
    for i in range(1, height + 1):
        if align.startswith("r"):
            print(" " * (height - i) + "*" * i)
        else:
            print("*" * i)

def main():
    try:
        h = int(input("Enter number of rows (positive integer): ").strip())
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return

    if h <= 0:
        print("Number of rows must be a positive integer.")
        return

    align = input("Alignment ([L]eft/[R]ight) : ").strip() or "L"
    print_right_angled_triangle(h, align)

if __name__ == "__main__":
    main()