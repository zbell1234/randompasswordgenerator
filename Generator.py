from Validator import Validator as validator
import random
import string
import pwinput

class Generator:
    def __init__(self, validator):
        self.validator = validator

    def genPassword(self):
        allString = string.ascii_letters + string.digits + string.punctuation
        pw = "".join(random.sample(allString, random.randrange(10,20)))
        while not self.validator.validate(pw):
            pw = "".join(random.sample(allString, random.randrange(10,20)))
        return pw

def main():
    options = {"keyboardPatterns": True}
    val = validator(options)
    gen = Generator(val)
    pw = gen.genPassword()
    print(pw)

if __name__ == '__main__':
    main()