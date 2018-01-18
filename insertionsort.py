def insertionSort(lyst):
	print lyst, '<<<unsorted'
	i = 1
	while i < len(lyst):
		itemToInsert = lyst[i]
		j = i - 1
		while j >= 0:
			if itemToInsert < lyst[j]:
				lyst[j+1] = lyst[j]
				j = j - 1
				print lyst
			else:
				break
		lyst[j+1] = itemToInsert
		i = i + 1
		print lyst
