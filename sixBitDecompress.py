encodings = {
	'a': 1,
	'b': 2,
	'c': 3,
	'd': 4,
	'e': 5,
	'f': 6,
	'g': 7,
	'h': 8,
	'i': 9,
	'j': 10,
	'k': 11,
	'l': 12,
	'm': 13,
	'n': 14,
	'o': 15,
	'p': 16,
	'q': 17,
	'r': 18,
	's': 19,
	't': 20,
	'u': 21,
	'v': 22,
	'w': 23,
	'x': 24,
	'y': 25,
	'z': 26,
	'A': 27,
	'B': 28,
	'C': 29,
	'D': 30,
	'E': 31,
	'F': 32,
	'G': 33,
	'H': 34,
	'I': 35,
	'J': 36,
	'K': 37,
	'L': 38,
	'M': 39,
	'N': 40,
	'O': 41,
	'P': 42,
	'Q': 43,
	'R': 44,
	'S': 45,
	'T': 46,
	'U': 47,
	'V': 48,
	'W': 49,
	'X': 50,
	'Y': 51,
	'Z': 52
}


def char_to_bit(char):
	num = ord(char)
	convert = unichr(num)
	ans = bin(num)

	return ans[0] + ans[2:]


def make_eight_bit(num):
	bin_str = num
	while len(bin_str) < 8:
		bin_str = '0' + bin_str
	return bin_str


def six_bit_byte_to_number(string):
	num = 0
	for i in range(len(string)):

		first = int(string[i])
		exponent =  5 - i
		foo = 2 ** exponent
		answer = first * foo
		
		num = num + answer

	return num


f = open("encodedOutput.dat", "r+b")

for i in f:
	d = list(i)

new_ary = [char_to_bit(i) for i in d]

eightbit_ary = [make_eight_bit(i) for i in new_ary]

temp = ''.join(eightbit_ary)

sixbit_ary = [temp[i:i+6] for i in range(0, len(temp), 6)]

final_ary = []
for i in range(len(sixbit_ary)):
	char_data = six_bit_byte_to_number(sixbit_ary[i])
	for k in encodings:
		if encodings[k] == char_data:
			final_ary.append(k)

f2 = open("decompressedOutput.dat", 'wb')
for i in final_ary:
	f2.write(i)
f2.close()




