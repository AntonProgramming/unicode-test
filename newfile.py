def unicode_test (value):
	import unicodedata
	name=unicodedata.name (value)
	print('value="%s", name="%s" ' %(value, name))
	print(name.encode ('utf-8'))
	print(name.encode('iso-8859-1'))
	print(name.encode('windows-1252'))
	#print(name.encode('unicode'))
	print(name.encode('utf-16'))
	a=name.encode('utf-16')
	print(type(a))
	#print(name.encode('ucs-2'))
	print(name.encode('ascii'))
#	print(name.decode('Unicode'))

unicode_test (input('Input a sign:'))