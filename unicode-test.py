def unicode_test (value):
	import unicodedata
	name=unicodedata.name (value)
	value2=unicodedata.lookup(name)
	print('value="%s", name="%s",value2="%s" ' %(value, name, value2))

unicode_test('\u00e9')
print(len('\u00e9'))

value='\u00e9'
print (value.encode('utf-8'))
print(value.encode('ascii', 'ignore'))
print (value)
unicode_test(input( ))