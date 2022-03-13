import random

def create_passwd(passwd):
    former_passwd = passwd
    passwd = list(passwd)
    capital_letters = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
    smaller_letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    number_counter = 0
    for symbol in passwd:
        try:
            if type(int(symbol)) == int:
                number_counter += 1
        except:
            continue

    if number_counter < 2:
        passwd.insert(0,str(random.randint(1,10)))
        passwd.insert(0, str(random.randint(1, 10)))


    def check_capital_letter():
        for symbol in capital_letters:
            if symbol in passwd:
                return True
        return False

    check_capital_letter = check_capital_letter()

    if not check_capital_letter:
        counter = 0
        for symbol in passwd:
            if symbol in smaller_letters:
                passwd[counter] = capital_letters[smaller_letters.index(symbol)]
            else:
                counter += 1

    if 'a' in passwd:
        passwd[passwd.index('a')] = '@'

    if 'i' in passwd:
        passwd[passwd.index('i')] = '!'

    if 'b' in passwd:
        passwd[passwd.index('b')] = '8'

    if 'o' in passwd:
        passwd[passwd.index('o')] = '0'

    passwd = "".join(passwd)

    if former_passwd == passwd:
        print('Your password is secure !')
    else:
        print('It is not secure you should use : ' + passwd)



user_passwd = input('Enter your password :')

create_passwd(user_passwd)



