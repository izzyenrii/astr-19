import numpy as np
import math as math

#first we return the value of sine
def sign(x):
	return np.sin(x)

#then we return the value of cosine
def cosign(x):
	return np.cos(x)

def main():
	a = 2*math.pi
	b = a/1000
	for x in np.arange(0,a,b):
		print(f"sin(x) = {x} {np.sin(x)} cos(x) = {np.cos(x)}")

if __name__ == "__main__":
    main()