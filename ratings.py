def create_ratings_dict(filename):
	"""Given a file of restaurants and ratings, return dictionary of key value pairs."""

	create_dict = {}
	
	#Add restaurants and ratings to dict
	with open(filename) as ratings:
		for line in ratings:
			pair = line.strip().split(":")
			create_dict[pair[0]] = pair[1]

	return create_dict


def add_new_rating(ratings_dict):
	"""Prompt user for new restaurant and corresponding rating, and return tuple."""

	new_restaurant = str.capitalize(input("Enter restaurant: "))
	new_rating = input("Enter rating out of 5: ")

	while is_rating_valid(new_rating) is False:
		print("Please enter a valid integer rating between 1 and 5.")
		new_rating = input("Enter rating: ")

	ratings_dict[new_restaurant] = new_rating

	return ratings_dict


def is_rating_valid(user_input):
	try:
		return int(user_input) >= 1 and int(user_input) <=5 and user_input.isdigit()
	except:
		return False


def print_ratings(ratings_dict):
	# Sort and print restaurant ratings
	for item in sorted(ratings_dict):
		print("{} is rated at {}.".format(item,ratings_dict[item]))


def choose_option(ratings_dict):

	while True:
		print("What would you like to do?")
		choice = input("A) See all ratings. B) Add and rate a resturant. C) Quit. ")

		if choice.lower() == "a":
			print_ratings(ratings_dict)
		elif choice.lower() == "b":
			ratings_dict = add_new_rating(ratings_dict)
		elif choice.lower() == "c":
			break
		else:
			print("Invalid input")


### MAIN ###
ratings_dict = create_ratings_dict("scores.txt")
choose_option(ratings_dict)

print("Thanks for using our ratings tool :) Good bye!")


