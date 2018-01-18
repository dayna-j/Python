#  Given an int n, return the absolute difference between n and 21,
#  except return double the absolute difference if n is over 21.

def diff21(n):
	if n<=21:
		diff= n - 21
		if diff <= 0:
			diff=diff*(-1)
			return diff
	else:
		diff = n - 21
		return 2*diff
	
