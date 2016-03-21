

def read_into_dict(level):
	"""
	  Function will return a dictinary. 
	   The dictionary will contain the entire high-score
	    list for the current level like this: 
	     { Name1: [Points, Time-stamp, Duration],
	       Name2: [Points, Time-stamp, Duration] }
	       ....
	       ----------------------------- Jonas ----
	"""
	
	file = open('Highscorelists\level{0}.txt'.format(level), 'r')

	# DICT-FORMAT -> "Name : [points, time_stamp, clock_diff]"
	highscore_dict = {} 
	line_cache = []

	while True:
		line_cache_raw = file.readline()
		line_cache = line_cache_raw.replace("\\n", "") # Removes "\n" from strings 
		if line_cache == "":                           # This means end of file
			break
		else:
			first_div = line_cache.index(",")        # Finds the first comma

			#   DICTIONARY              [KEY]      =  [VALUE1, VALUE2, VALUE3]
			highscore_dict[line_cache[:first_div]] = line_cache[first_div + 2:]

	file.close()

	return highscore_dict


def write_from_dict(level, highscore_dict):
	"""
	  Function writes from a modified dictionary, 
	   back to the file in this format: 
	   	name, points, Time-stamp, Duration, level, game\n
	   	-------------------------- Jonas ----
	   """

	file = open('Highscorelists\level{0}.txt'.format(level), 'w')
	while True:	
		try:
			item_pop = str(highscore_dict.popitem())
			for i in item_pop:
				i = i.strip("[")
				i = i.strip("]")
				i = i.strip("(")
				i = i.strip(")")
				i = i.strip("'")
				file.write(i)
			file.write("\n")
		except KeyError:
			break

	file.close()

	return 0


def store_data(new_data):
	""" new_data is a list of:
	- user_name   index [0]
	- points      index [1]
	- time_stamp  index [2]
	- clock_diff  index [3]
	- level_int   index [4]
	- Game_name   index [5]
	------------ Jonas ---"""

	level = new_data[4]     #Gets a integer between 1-4
	
	highscore_dict = read_into_dict(level)
	highscore_dict[new_data[0]] = [new_data[1:]]
	write_from_dict(level, highscore_dict)







