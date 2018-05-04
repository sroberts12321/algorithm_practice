num_list = [2,3,4,500,6,7,8,152]

is_greatest = 0

#finding greatest
for number in num_list:
	if number > is_greatest:
		is_greatest = number

print(f"\n{is_greatest} is the greatest value in the array")


#using the greatest value to compare all other numbers in array and find the least
for number in num_list:
	if number < is_greatest:
		is_greatest = number

print(f"\n{is_greatest} is the lowest value in the array\n")