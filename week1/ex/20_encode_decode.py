letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encode(kkk):
	kkk1 = ""
	for i in kkk:
		if i in letter:
			if letter.index(i)<13:
				kkk1+=letter[letter.index(i)+13]
			else:
				kkk1 += letter[letter.index(i) - 13]
	return kkk1
meow = int(input("Press 1 to encode\nPress 2 to decode"))
if meow == 1:
	woff=input('Enter string to encode')
	print(f'The encode text is:{encode(woff)}')
	lol=input('Do you want to continue? [Y/N]' )
	if lol=="Y":
		meow = int(input("Press 1 to encode\nPress 2 to decode"))
		if meow == 1:
			woff = input('Enter string to encode')
			print(f'The encode text is:{encode(woff)}')
		elif meow == 2:
			woff = input('Enter string to decode')
			print(f'The encode text is:{encode(woff)}')
	elif lol == 'N':
		print("Function end")
if meow == 2:
	woff=input('Enter string to decode')
	print(f'The decode text is:{encode(woff)}')
	lol=input('Do you want to continue? [Y/N]' )
	if lol=="Y":
		meow = int(input("Press 1 to encode\nPress 2 to decode"))
		if meow == 1:
			woff = input('Enter string to encode')
			print(f'The encode text is:{encode(woff)}')
		elif meow == 2:
			woff = input('Enter string to decode')
			print(f'The encode text is:{encode(woff)}')
	elif lol=='N':
		print("Function end")