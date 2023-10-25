# Keenan Rutledge
def main():
	print('Menu \n-------------\n1. Encode\n2. Decode\n3. Quit')
	print('Please enter an option:')


def encode(string):
	encode_data = []
	for item in string:
		if item.isdigit():
			encode_data.append(int(item) + 3)
	sep = ''
	final_encode = sep.join(str(i) for i in encode_data)
	return final_encode

def decode(string):
	decodeList = list(string)
	decodedPass = ""
	for item in decodeList:
		item = int(item)
		item -= 3
	decodedPass = str(decodeList)
	return decodedPass


if __name__ == '__main__':
	main()
	op = int(input())
	encoded_pass = None
	data = None
	while op != 3:
		if op == 1:
			print('Please enter your password to encode:')
			data = str(input())
			encoded_pass = encode(data)
			print('Your password has been encoded and stored!')
			main()
			op = int(input())
		elif op == 2:
			decodedpass = decode(encoded_pass)
			print("The encoded password is: " + encoded_pass + ", and the original password is: " + decodedpass + ".")
		if op == 3:
			exit
