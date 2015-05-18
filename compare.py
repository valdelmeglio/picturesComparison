def dhash(image, hash_size = 8):
	image = image.convert('L').resize(
		(hash_size + 1, hash_size),
		#Image.ANTIALIAS,
		)


	pixels = list(image.getdata())

	difference = []
	for row in xrange(hash_size):
		for col in xrange(hash_size):
			pixel_left = image.getpixel((col, row))
			pixel_right = image.getpixel((col + 1, row))
			difference.append(pixel_left > pixel_right)

	decimal_value = 0
	hex_string = []
	for index, value in enumerate(difference):
		if value:
			decimal_value += 2**(index % 8)
		if (index % 8) == 7:
			hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
			decimal_value = 0

	return ''.join(hex_string)


def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))
