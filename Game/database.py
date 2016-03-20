

def store_data(new_data):
	""" new_data is a list of:
	- level_name  index [0]
	- user_name   index [1]
	- points      index [2]
	- time_stamp  index [3]
	- clock_diff  index [4]
	------------ Jonas ---"""

	#-------- READ FILE INTO highscore_dict = {} --------#

	level = new_data[0]     #Gets a integer between 1-4
	file = open('level{0}.txt'.format(level), 'r')

	highscore_dict = {} # Name : [points, time_stamp, clock_diff]
	line_cache = []

	while True:
		line_cache_raw = file.readline()
		line_cache = line_cache_raw.replace("\\n", "")
		if line_cache == "":
			print("END OF FILE")
			break
		else:
			print(line_cache)
			first_div = line_cache.index(",")
			print(first_div)
			highscore_dict[line_cache[:first_div]] = line_cache[first_div + 2:]

	file.close()

	# -------- MODIFY highscore_dict={} with new_data ------

	highscore_dict[new_data[1]] = [new_data[2:]]
	print(highscore_dict)

	# ------- WRITE highscore_dict BACK TO FILE -----------

	file = open('level{0}.txt'.format(level), 'w')
	while True:	
		try:
			item_pop = str(highscore_dict.popitem())
			print(item_pop)

			for i in item_pop:
				i = i.strip("dict_items")
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





