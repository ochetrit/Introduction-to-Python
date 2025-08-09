import sys

def main(av):

	if len(av) == 1:
		return

	try:
		assert len(av) <= 2, "more than one argument is provided"
		assert av[1].isnumeric() or av[1][0] == '-' and av[1][1:].isdigit(), "argument is not an integer"

	except AssertionError as e:
		print(f'AssertionError: {e}')
		return 1

	nb = int(av[1])
	if nb % 2 == 0:
		print("I'm Even.")
	else:
		print("I'm Odd.")



if __name__ == "__main__":
	main(sys.argv)
