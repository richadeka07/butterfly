import sys

#!/usr/bin/env python3
"""
butterfly.py
Print a butterfly pattern using '*'.

Usage:
    python butterfly.py 5
    (or run without args and enter a number when prompted)
"""


def butterfly(n: int) -> None:
        if n <= 0:
                return
        # upper half
        for i in range(1, n + 1):
                left = '*' * i
                gap = ' ' * (2 * (n - i))
                right = '*' * i
                print(left + gap + right)
        # lower half
        for i in range(n-1, 0, -1):
                left = '*' * i
                gap = ' ' * (2 * (n - i))
                right = '*' * i
                print(left + gap + right)

def main():
        n = None
        if len(sys.argv) > 1:
                try:
                    n = int(sys.argv[1])
                except ValueError:
                        pass
        if n is None:
                try:
                        n = int(input("Enter number of rows (n): ").strip())
                except ValueError:
                        n = 5
        butterfly(n)
if __name__ == "__main__":
        main()