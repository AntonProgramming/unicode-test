def unicode_test (value):
	import unicodedata
	name=unicodedata.name (value)
	value2=unicodedata.lookup(name)
	print('value="%s", name="%s",value2="%s" ' %(value, name, value2))

unicode_test('\u00e9')
print(len('\u00e9'))