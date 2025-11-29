
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
    

    

