'''
##### Task 1 Percent Error
Ask the user to input the following:
* the expected number
* the actual result
Calculate the percent difference between the two results. Round your answer to 2 decimal places

```
https://www.skillsyouneed.com/num/percent-change.html

Sample Output:
Enter expected: 10
Enter actual : 9
The percent difference is -10.0%

Enter expected: 12
Enter actual : 14
The percent difference is 16.67%
```
'''
import math
b = float(input("what is the expected number "))
a = float(input("what is the actual result "))
per_dif = (abs((a-b)) / ((a+b)/2))*100
per_dif = round(per_dif, 2)
print(f"the percent difference is {per_dif}")
print("that website doesn't show the right way to do percent difference by the way")
print("your supposed to do it by (((V1-V2) / ((V1+V2)/2))*100)")