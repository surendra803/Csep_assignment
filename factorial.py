def recur_factorial(n):
	if n==1:
		return n
	else:
		return n*recur_factorial(n-1)
num=int(input())
if num<0:
	print("Sorry,factorial does not exise")
elif num==0:
	print("factorial of 0 is 1")
else:
	print("factorial of",num,"is",recur_factorial(num))
