import string

class Validator:
    def __init__(self, options):
        self.results = {}
        self.options = options

    def checkLength(self, input):
        return len(str(input)) >= 10

    def uniqueChars(self, input):
        return len(set(str(input))) >= 5

    def checkUpper(self, input):
        for ch in str(input):
            if ch.isupper():
                return True
        return False

    def checkLower(self, input):
        for ch in str(input):
            if ch.islower():
                return True
        return False

    def checkSpecial(self, input):
        specials = string.punctuation
        if any(c in specials for c in str(input)):
            return True
        return False

    def checkNums(self, input):
        nums = ['0','1','2','3','4','5','6','7','8','9']
        if any(n in nums for n in str(input)):
            return True
        return False

    def checkRepeating(self, input, times=4):
        temp = str(input).lower()
        i = 0
        while i < (len(temp) - times):
            if temp[i:i + times] == temp[i]*times:
                return True
            i += 1
        return False

    def checkKeyboardPatterns(self, input, times=3):
        rows = ["1234567890", "qwertyuiop", "asdfghjkl", "zxcvbnm"]
        revRows = [row[::-1] for row in rows]
        rows.append(revRows)
        for index in range(0, len(str(input))-times-1):
            sequence = str(input)[index:index+times]
            for i in range(0, len(rows)-1):
                if sequence in rows[i]:
                    return False
        return True

    
    def checkRequired(self, input):
        self.results['Length'] = self.checkLength(input)
        self.results['Unique Characters'] = self.uniqueChars(input)
        self.results['Uppercase Letter(s)'] = self.checkUpper(input)
        self.results['Lowercase Letter(s)'] = self.checkLower(input)
        self.results['Special Character(s)'] = self.checkSpecial(input)
        self.results['Number(s)'] = self.checkNums(input)
        self.results['Repeating'] = not self.checkRepeating(input)
        self.checkOptionals()
        return self.results

    def checkOptionals(self):
        if self.options['keyboardPatterns']:
            self.results['Keyboard Patterns'] = self.checkKeyboardPatterns(input)


    def validate(self, input):
        password = input
        results = self.checkRequired(password)
        for key, result in results.items():
            test = "Passed" if result else "Failed"
            print("Condition " + str(key) + ": " + test)
        fin = not False in set(results.values())
        return fin