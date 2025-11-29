bits = int (input("Enter number of bits= "))
mb = bits/1000000
gb = bits/1000000000*8
tb = bits/1000000000000*8

print("Bits to megabytes=", mb, "MB")
print("Bits to gigabytes=", gb, "GB")
print("Bits to terabytes=", tb, "TB")