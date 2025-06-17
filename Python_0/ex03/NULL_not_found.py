def NULL_not_found(object: any) -> int:
	types_dict = {
		NoneType : "List :",
		: "Tuple :",
		set: "Set :",
		dict: "Dict :",
		str: f"{object} is in the kitchen :"
		}
	
	my_type = type(object)
	aff = types_dict.get(my_type)
	if aff:
		print (aff, my_type)
	else:
		print("Type not found")
	return 42


