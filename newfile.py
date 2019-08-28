def unicode_test (value):
	import unicodedata
	name=unicodedata.name (value)
	print('value="%s", name="%s" ' %(value, name))
	#print(decoding)

unicode_test(input('Input a sign:'))