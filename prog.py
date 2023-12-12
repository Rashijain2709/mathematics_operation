# Global Variables

a = 1
b = 2

# This method is used to add two number
def add(a, b):
	return a + b

# This method is used to subtract two number
def sub(a, b):
	return a - b

def main():
	print("addition of two numbers: " + str(add(a, b)))
	print("substraction of two numbers: " + str(sub(a, b)))
	
if __name__ == '__main__':
	main()

