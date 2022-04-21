import numpy as np

def sign(x):
	return np.sin(x)
# end sign

def cosign(x):
	return np.cos(x)
#end cosign

def main():
	sine = sign(int(input()))
	cosine = cosign(int(input()))

	print(sine, cosine)

if __name__ == '__main__':
	main()
#here we will define our main program function
