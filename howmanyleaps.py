def how_many_leaps(startyr, nyrs):
	n=0
	years=range(startyr,startyr+nyrs+1)
	for yr in years:
		n+=is_leap_year(yr)
	return n