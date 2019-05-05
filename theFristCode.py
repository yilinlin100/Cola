search = '168'
num_a = '1368-168-0006'
num_b = '1681-222-0006'

#print(search + ' is at '+ str(num_a.find(search)) +
#     ' to ' + str(num_a.find(search) + len(search)) + ' of num_a ' )

#city = input('write down the name of city:')

def function(arg):
    y = arg / 1000
    return str(y) + 'kg'
y1 = function(350)
#print(y1)

def function(arg1, arg2):
    yy = (arg1 ** 2 + arg2 ** 2) ** (1/2)
    return  'The right triangle third side\'s length is {}' .format(yy)
y2 = function(3,4)
#print(y2)

def text_create(name,msg):
    desktop_path = 'D:/PycharmProjects/untitled/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path,'w')
    file.write(msg)
    file.close()
    print('done')

#text_create('hello','hello world')

def text_filter(wold,cencored_wold = 'lame',change_wold = 'awesome'):
    return wold.replace(cencored_wold,change_wold)
#cc = text_filter('Python is lame!')
#print(cc)


def text_censored_create(name,msg):
    clean_msg = text_filter(msg)
    text_create(name,clean_msg)

text_censored_create('Try','lame!lame!')
#print(text_censored_create('Try','lame!lame!') )




def account_login():
    passwold = input('Passwold:')
    paasswold_correct = passwold == '12345'
    if paasswold_correct:
        print('login succuss!')
    else:
        print('worry passwold or invalid input!')
        account_login()
account_login()

passwold_list = ['*#*#,','12345']
def account_login():
    passwold = input('Passwold:')
    passwold_correct = passwold == passwold_list[1]
    passwold_reset = passwold == passwold_list[0]
    if passwold_correct:
        print('login success!')
    elif passwold_correct:
        new_passwold = input('enter a new passwold:')
        passwold_list.append(new_passwold)
        print('your passwold has changes successfully')
        account_login()
    else:
        print('worry passwold or invalid input')
        account_login()
account_login()

songlist = ['Holy Diver', 'Thunderstruck','Rebel']
for song in songlist:
    if song == 'Holy Diver':
        print(song,' - Dio')
    elif song == 'Thunderstruck':
        print(song,' - AC')
    else:
        print(song,' - David')

for i in range(1,10):
    for j in range(1,10):
        print('{}*{}={}'.format(i,j,i*j))



passwold_list = ['*#*#,','12345']
def account_login():
    tries = 3
    while tries > 0:
        passwold = input('Passwold:')
        passwold_correct = passwold == passwold_list[1]
        passwold_reset = passwold == passwold_list[0]
        if passwold_correct:
            print('login success!')
        elif passwold_correct:
            new_passwold = input('enter a new passwold:')
            passwold_list.append(new_passwold)
            print('your passwold has changes successfully')
            account_login()
        else:
            print('worry passwold or invalid input')
            tries = tries - 1
            print(tries,'time left')
    else:
         print('your account has been suspended')
account_login()
