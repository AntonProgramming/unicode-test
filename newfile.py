def unicode_test (value):
	import unicodedata
	name=unicodedata.name (value)
	print('value="%s", name="%s" ' %(value, name))
	print(name, encoding ='utf-8')

unicode_test(input('Input a sign:'))