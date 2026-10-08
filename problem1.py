#!python3

# Canada Income Tax Calculator part I

'''
It's tax season!  Nobody loves doing taxes, so EVERYONE uses computers to help them.  We will use
Python to determine Federal and Provincial Income Tax.

The Canadian income tax system is a tiered system, which means you pay different percentages of
your income for different parts of your income.
You pay 15% tax on the first 49020 you earn.  If you earn more than this amount, you pay
20.5% on amounts over 49020 that are less than 98040
26% on amounts over 98040 but less than 151978
29% on amounts over 151978 but less than 216511
33% on amounts over 216511

Write a program to calculate the amount of Federal Income Tax for people who earn over 100,000 but less than 150,000

Example:
Enter your income: 125000
Your federal income tax is: 24411.7

'''
import math
i = float(input("enter your income "))
t = min(i, 49020)*0.15
fi = max(i-49020, 0)
t = min(fi, 49020)*0.205+t
fi = max(i-98040, 0)
t = min(fi, 53938)*0.26+t
fi = max(i-151978, 0)
t = min(fi, 64533)*0.29+t
fi = max(i-216511, 0)
t = fi*0.33+t
t = round(t, 2)
print(f"you have to pay {t}$ in taxes which means you have {i-t}$ left")