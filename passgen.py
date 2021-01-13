import random
import string
length = int(input('Enter the size of password :'))
if length > 20:
    raise Exception('Invalid! length try with lower one')
elif length < 1:
    raise Exception('Password cannot be of \'zero\' length')
else:

    def paas_gen(length):
        result = string.ascii_letters + string.digits + string.printable
        pasword = ''.join((random.choice(result)for i in range(length)))
        print('Alphanumeric password of \'{}\' character is : {}'.format(
            length, pasword))
        print(' ' * 45 + '-' * length)
    paas_gen(length)
random.seed(2)
