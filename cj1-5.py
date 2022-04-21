import numpy as np

#here we will define our main program function
def main():
	a = 2*np.pi     #labeling our a variable
	b = a/1000      #labeling the b variable
	for x in np.arange(0,a,b):
		#print the sin(x)
		print("the sin of", x, "is", np.sin(x))
#calling the main function
if __name__ == "__main__":
	main()