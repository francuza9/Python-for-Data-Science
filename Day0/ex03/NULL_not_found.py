def NULL_not_found(object: any) -> int:
	if object is None:
		print(f"Nothing: {None} {type(object)}")
	elif type(object) is float and object != object:
		print(f"Cheese: {float('NaN')} {type(object)}")
	elif object == 0 and type(object) is int:
		print(f"Zero: {object} {type(object)}")
	elif object == '' and type(object) is str:
		print(f"Empty: {type(object)}")
	elif object is False and type(object) is bool:
		print(f"Fake: {object} {type(object)}")
	else:
		print("Type not Found")
		return 1
	return 0