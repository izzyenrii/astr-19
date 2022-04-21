import numpy as np

class rats:
        
	def __init__(self, length_of_arms=0.0, length_of_legs=1.0, number_of_legs=4, number_of_eyes=2, does_it_have_a_tail=True, is_it_furry=True):
		self.arm_length = length_of_arms
		self.leg_length = length_of_legs
		self.leg_number = number_of_legs
		self.eye_number = number_of_eyes
		self.tail = does_it_have_a_tail
		self.fur = is_it_furry

	def rat(self):

		print(f"The length of a rats arms are {self.arm_length}. rats don't have arms.")
		print(f"The length of a rats legs are {self.leg_length} feet.")
		print(f"A rat has {self.leg_number} legs.")
		print(f"A rat has {self.eye_number} eyes.")
		print(f"Does a rat have a tail? {self.tail}")
		print(f"Is an rat furry? {self.fur}")
def main():
	a = rats(0.0,1.0,4,2,True,False)
	a.rat()
	print(a.arm_length, a.leg_length, a.leg_number, a.eye_number, a.tail, a.fur)
if __name__ == "__main__":
        main()