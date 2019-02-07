#part1
def street_info():
	tuple_list = []
	file = open("Street_Centrelines.csv","r")
	file.readline()
	for column in file:
		column =  column.split(",")
		tuple_list.append((column[2],column[4],column[7],column[8]))
	return tuple_list


#part2
def hist_maintenance():
	maintenance = dict()
	file = open("Street_Centrelines.csv","r")
	file.readline()
	for line in  file:
		line = line.split(",")
		maintenance[line[12]] = maintenance.setdefault(line[12],0) + 1
	return maintenance


#part3
def unique():
	owner = []
	file = open("Street_Centrelines.csv","r")
	file.readline()
	for line in file:
		line = line.split(",")
		owner.append(line[11])
	owner =  list(set(owner))
	return owner


print(street_info())
print(hist_maintenance())
print(unique())
