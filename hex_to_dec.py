from ast import literal_eval

hexnum = '0x' + input("Enter a Hexidecimal number: ")

res = literal_eval(hexnum)

print(f'The decimal value is {str(res)}')
