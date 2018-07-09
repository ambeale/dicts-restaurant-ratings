def restaurant_ratings(file_ratings):
	"""Restaurant rating lister."""
	
	ratings = open(file_ratings)
	ratings_dict = {}
	
	#Add restaurants and ratings to dict
	for line in ratings:
		pair = line.strip().split(":")
		ratings_dict[pair[0]] = pair[1]
	
	new_restaurant = str.capitalize(input("Enter restaurant: "))
	new_rating = input("Enter rating out of 5: ")

	ratings_dict[new_restaurant] = new_rating

	# Sort and print restaurant ratings
	for item in sorted(ratings_dict):
		print("{} is rated at {}.".format(item,ratings_dict[item]))


restaurant_ratings("scores.txt")