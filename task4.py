#!python3

"""
Write a program to ask the user to input a length in centimeters. Convert this into feet and inches.  Round your inches to the nearest whole inch.
You will likely need to make use of at least one of the following:
* % modulus
* math.floor()

Sample output:
```
Enter a length in centimeters: 172
172 centimeters is 5 feet and 8 inches

Enter a length in centimeters: 32
32 centimeters is 1 feet and 1 inches
```
"""
import math
cm = float(input("what is the length in cm "))
inc = cm/2.54
rin = math.fmod(inc, 12)
ft = (inc-rin)/12
print(f"{cm:g}cm in feet and inchs is {ft:.0f}ft{rin:.0f}in")