
def restaurant_ratings(file_ratings):
	"""Restaurant rating lister."""
	
	ratings = open(file_ratings)
	ratings_dict={}
	for line in ratings:
		pair = line.strip().split(":")
		ratings_dict[pair[0]] = pair[1]
	#print(ratings_dict)	

	for item in sorted(ratings_dict):
		print("{} is rated at {}.".format(item,ratings_dict[item]))

restaurant_ratings("scores.txt")



# put your code here
