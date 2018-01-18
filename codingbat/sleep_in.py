#def sleep_in(weekday, vacation):
#	if not weekday:
#		return True
#	if weekday:
#		if not vacation:
#			return False
#		elif vacation:
#			return True

def sleep_in(weekday, vacation):
	if not weekday or vacation:
		return True
	else:
		return False
