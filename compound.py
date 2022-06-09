from matplotlib import pyplot as plt
def compound_interest(P,r,t):
	CI=((P*(1+(r/100))**t) - P)
	print(CI)
P=float(input( "Enter the principle amount  "))
r=float(input("Enter the rate "))
t= float(input("Enter the time period"))
compound_interest(P,r,t)
#plt.plot(t,CI)
#plt.show()
