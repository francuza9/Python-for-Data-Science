
def NULL_not_found(object: any) -> int:
	if object == None:
		print("Nothing:", object, type(object))
	elif type(object) == float and object != object:
		print("Cheese:", object, type(object))
	elif object == 0 and type(object) == int:
		print("Zero:", object, type(object))
	elif object == "" and type(object) == str:
		print("Empty:", object, type(object))
	elif object == False and type(object) == bool:
		print("Fake:", object, type(object))
	else:
		print("Type not Found")
		return 1
	return 0
