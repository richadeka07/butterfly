'''
#!/usr/bin/env python3
# hollow square.py
# Prints a hollow square made of '*' characters.

def draw_hollow_square(n, ch='*'):
    if n <= 0:
        return
    if n == 1:
        print(ch)
        return
    print(ch * n)
    interior = '\u00A0' * (n - 2)
    for _ in range(n - 2):
        print(ch + interior + ch)
    print(ch * n)

def main():
    try:
        s = input().strip()
        if not s:
            raise ValueError
        n = int(s)
        if n <= 0:
            raise ValueError
    except Exception:
        print("Please provide a positive integer size (e.g. 5).")
        return
'''

def print_hollow_square_with_numbers():
    while True:
        try:
            size = int(input("Enter a positive number: "))
            if size > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input.")

    for i in range(1, size + 1):  # Outer loop for rows
        for j in range(1, size + 1):  # Inner loop for columns
            if i == 1 or i == size or j == 1 or j == size:
                print(i, end=" ")  # Print the row number for border positions
            else:
                print(" ", end=" ")  # Print space for hollow part
        print()  # Move to the next line after each row

print_hollow_square_with_numbers()    

