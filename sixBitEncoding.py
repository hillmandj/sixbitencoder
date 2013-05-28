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
	'Z': 52,
	' ': 53,
	'.': 54,
	'!': 55,
	'\n':56
}

def betterSixBit(num):
	six_bit_str = ''
	while num:
		six_bit_str = str(num % 2) + six_bit_str
		num = num >> 1
	if not num:
			while len(six_bit_str) < 6:
				six_bit_str = '0' + six_bit_str
	return six_bit_str


def compress_six_bit(ary):
	temp = ''.join(ary)
	final_list = [temp[bit:bit+8] for bit in range(0, len(temp), 8)]
	return final_list


def byte_printer(string):
	num = 0
	for i in range(len(string)):
		first = int(string[i])
		exponent =  7 - i
		foo = 2 ** exponent
		answer = first * foo
		num = num + answer
	return chr(num)


x = open('data.dat')
s = x.read()
ary = [i for i in s]

encoded_ary = []
for i in range(len(ary)):
	char_data = ary[i]
	encoded_num = encodings[char_data]
	encoded_ary.append(betterSixBit(encoded_num))
	
compressed_ary = compress_six_bit(encoded_ary)

f = open("encodedOutput.dat", "wb")
for i in compressed_ary:
	d = byte_printer(i)
	f.write(d)
f.close()



