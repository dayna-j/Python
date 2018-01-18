#Given an array of ints, return True if .. 1, 2, 3, .. appears in the
# array somewhere. 

def array123(nums):
    string = ''
    for eachNum in nums:
        string = string+str(eachNum)
    
    return '123' in string

