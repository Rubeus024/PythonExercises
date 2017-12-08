import scipy.integrate as integrate


myList=list(map(lambda x: x**2,range(1,12) ))
print(myList)
result = integrate.trapz(myList,None,0.1)
print(result)
result = integrate.trapz(myList,None,1)
print(result)
