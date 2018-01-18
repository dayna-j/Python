#IF NEGATIVE IS TRUE, RETURN TRUE IF BOTH NUMBERS ARE NEGATIVE
#OTHERWISE, RETURN TRUE IF ONE NUMBER IS POSITIVE AND THE OTHER IS NEGATIVE

def pos_neg(a,b,negative):
	if negative:
        return (a < 0 and b < 0)
    else:
        return ((a < 0 and b > 0) or (a > 0 and b < 0))
