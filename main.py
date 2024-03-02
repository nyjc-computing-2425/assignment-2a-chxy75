num = input('Enter a number (decimal or integer): ')
# type your code here
clear = num.strip(' ').lstrip('0').replace('.','')
sf = len(clear.lstrip('0'))


# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
