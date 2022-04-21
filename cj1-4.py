import numpy as np

class rats:
        
	def __init__(self, length_of_arms=0.0, length_of_legs=1.0, number_of_legs=4, number_of_eyes=2, does_it_have_a_tail=True, is_it_furry=True):
		self.arm_length = length_of_arms
		self.leg_length = length_of_legs
		self.leg_number = number_of_legs
		self.eye_number = number_of_eyes
		self.tail = does_it_have_a_tail
		self.fur = is_it_furry

	def rat():

		print(f"The length of an rats arms are {self.arm_length}. rats don't have arms.")
		print(f"The length of an rats legs are {self.leg} feet.")
		print(f"An rat has {self.leg_number} legs.")
		print(f"An rat has {self.eye_number} eyes.")
		print(f"Does a rat have a tail? {self.tail}")
		print(f"Is an rat furry? {self.fur}")
def main():
	a = rats()
	print(a.arm_length, a.leg_length, a.leg_number, a.eye_number, a.tail, a.fur)
if __name__ == "__main__":
        main()
