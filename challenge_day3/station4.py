def solution_station_4(input):
	for i in range(2, int(input/2)+1):
		if (input % i) == 0:
			return True
		break
	else:
		return False
