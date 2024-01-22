name = 'Bro'

print('{')
print('\tlength: ', len(name))
print('\t\"o\"_index: ', name.find('o'))
print('\tcapitalized: ', name.capitalize())
print('\tuppercased: ', name.upper())
print('\tlowlercased: ', name.lower())
print('\tis_digit: ', name.isdigit())
print('\tis_alphabetic: ', name.isalpha())
print('\tcount_of_\"o\"s: ', name.count('o'))
print('\treplacint_o_with_a: ', name.replace('o', 'a'))
print('\tlength: ', name*3)
print('}')