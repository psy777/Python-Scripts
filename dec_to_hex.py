input_number = int(input('Number: '))
numlist = []
new_numlist = []
al = []

def create_list(number):
    while number>1:
        number = number/16
        numlist.append(number)
    numlist.pop()

def smooth_list():
    for num in numlist:
        num = find_and_delete_decimals(num)
        new_numlist.append(int(num))

def create_al():
    al.append(input_number%16)
    for number in new_numlist:
        al.append(number%16)

def create_al_2():
    for n, i in enumerate(al):
        if i == 10:
            al[n] = 'a'
        if i == 11:
            al[n] = 'b'
        if i == 12:
            al[n] = 'c'
        if i == 13:
            al[n] = 'd'
        if i == 14:
            al[n] = 'e'
        if i == 15:
            al[n] = 'f'

def create_answer():
    for n, i in enumerate(al):
        al[n] = str(al[n])
    str1 = ''
    print(f'The hexidemal value is {str1.join(al[::-1])}')

def find_and_delete_decimals(string):
    sep = '.'
    newdiv=str(string)
    rest = newdiv.split(sep, 1)[0]
    return(int(rest))

def dec_to_hex():
    create_list(input_number)
    smooth_list()
    create_al()
    create_al_2()
    create_answer()

dec_to_hex()
