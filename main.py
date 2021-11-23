import os, random, string

class GeneratePassword:
    def __init__(self, lenght):
        self.lenght = lenght
        self.chars = string.ascii_letters + string.digits + '!@#$%^&*()'

    def start(self):
        answer = input('Would you like to generate a password?')
        try:
            if answer == 'yes' or answer == 'y':
                os.system('cls')
                print('The generated password is: ' + self.generateValue() + '\n\n')
                self.start()
            elif answer == 'no' or answer == 'n':
                os.system('cls')
                print('Bye!')
            else:
                os.system('cls')
                print('Choose between "yes" or "no"')
                self.start()
        except:
            print('Error')

    def generateValue(self):
        random.seed = (os.urandom(1024))
        return (''.join(random.choice(self.chars) for i in range(self.lenght)))

generator = GeneratePassword(15)
generator.start()   