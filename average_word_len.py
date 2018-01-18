#This program will return the average word length of a sentence entered
#by the user.

def main():
	
	strInput = raw_input('Enter your string: ')
	strInput = strInput.split()
	numWords = len(strInput)
	lenWords = 0
	for eachItem in strInput:
		lenWords = lenWords + len(eachItem)
	print ''
	
	average = float(lenWords)//numWords
	
	print 'The average word length is',average
