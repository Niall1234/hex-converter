from math import floor

letters = {
	10: "A",
	11: "B",
	12: "C",
	13: "D",
	14: "E",
	15: "F"
}

while True:
	
	hex_value = int(input("Enter decimal value: "))

	hex_list = []
       
	while hex_value > 16:
		hex_list.insert(0,str(hex_value % 16))
		hex_value = int(hex_value / 16) 
	
	if hex_value > 0:
		hex_list.insert(0,str(hex_value))

	for i in range(len(hex_list)):
		if int(hex_list[i]) > 9:
			hex_list[i] = letters[int(hex_list[i])]
	
	print("Hex value:" +  ("").join(hex_list))
