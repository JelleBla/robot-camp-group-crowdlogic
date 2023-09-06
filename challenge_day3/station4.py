def solution_station_4(input):
    if n > 1:
	for i in range(2, int(n/2)+1):
		if (n % i) == 0:
			return True
		break
	else:
		return False
