def max_end3(nums):
	
	big = bigger(nums[0],nums[-1])
	
	for i in range(len(nums)):
		nums[i] = big
	return nums


def bigger(a,b):
	if a >= b:
		return a
	else:
		return b
