# Python Program to find the Factorial of a number using Recursion
# Fact_Recur.Py
def fact(m):
  if m<=1:
    return 1
  else:
    return m*fact (m-1)
# Main Program
n=int (input("Enter the value of n:"))
print("the factorial of ",n,"is",fact (n))
