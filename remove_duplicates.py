names = ["Alex","John","Mary","Steve","John", "Steve"]

is_duplicate = []

for name in names:
	if name not in is_duplicate:
		is_duplicate.append(name)
		
print(is_duplicate)