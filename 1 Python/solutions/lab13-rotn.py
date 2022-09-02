# In class example of ROT-n to handle any rotation

alpha = 'abcdefghijklmnopqrstuvwxyz'

def encode_rot(string, n):
	n %= 26 # n loops around if greater than 26
	encoded = ''
	for char in string:
		index = alpha.find(char.lower())
		if index < 0:
			encoded += char
		elif index + n >= len(alpha):
			encoded += alpha[index+n-len(alpha)]
		else:
			encoded += alpha[index+n]
	return encoded


def decode_rot(string, n):
	n %= 26 # n loops around if greater than 26
	encoded = ''
	for char in string:
		index = alpha.find(char.lower())
		if index < 0:
			encoded += char
		elif index - n < 0:
			encoded += alpha[index-n+len(alpha)]
		else:
			encoded += alpha[index-n]
	return encoded


if __name__ == '__main__':
	# print(encode_rot(input("enter a string: "), int(input("enter your rotation offset: "))))
	for i in range(26):
		print(f'Encoded ROT-{i}: {encode_rot(alpha, i)} \nDecoded: {decode_rot(encode_rot(alpha,i),i)}\n')

main()
