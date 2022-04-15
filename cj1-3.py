#this program will defind the function f(x)
#and return x**3+8

import numpy as np
def f(x):
	return(x**3 + 8)

#main function to print result and 
#call f(x) with x = 9

def main():
	x = 9
	f(x)                         #defining f(x) as x = 9
	print(x,"cubed + 8 = ",f(x)) #printing the final result
	if(f(x)>27):                 #has to be larger than 27
		print(f(x),"is larger than 27, YAY!") 
		
#writing out the main if function

if __name__ == "__main__":
	main()