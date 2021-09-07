class Morse():
    def __init__(self):
        self.morse_code = dict()
        self.morse_code = {
        # dot==0  dash==1
        'A':'01',
        'B':'1000',
        'C':'0101',
        'D':'100',
        'E':'0',
        'F':'0010',
        'G':'110',
        'H':'0000',
        'I':'00',
        'J':'0111',
        'K':'101',
        'L':'0100',
        'M':'11',
        'N':'10',
        'O':'111',
        'P':'0110',
        'Q':'1101',
        'R':'010',
        'S':'000',
        'T':'1',
        'U':'001',
        'V':'0001',
        'W':'011',
        'X':'1001',
        'Y':'1011',
        'Z':'1100',
        # Digits
        '1':'01111',
        '2':'00111',
        '3':'00011',
        '4':'00001',
        '5':'00000',
        '6':'10000',
        '7':'11000',
        '8':'11100',
        '9':'11110',
        '0':'11111',
        #symbols
        ',':'110011',
        '?':'001100',
        '-':'100001',
        '.':'010101'

        }


    def toMorse(self, message):
        res = ''
        res_lst = list()
        for i in str(message):
            if i == ' ' or i == '  ':
                res_lst.append(i)
            elif str(i.upper()) in self.morse_code.keys():
                res_lst.append(self.morse_code.get(str(i.upper())))
                res_lst.append('|')
            else:
                pass
        for i in res_lst:
            res += str(i)
        return res

    def toText(self, code):
        res = ''
        item = ''
        for i in code.split('|'):
            if len(i.split(' ')) == 2:
                res += ' '
                for key, value in self.morse_code.items():
                    if value == i.split(' ')[1]:
                        res += key
            elif len(i.split(' ')) == 1:
                for key, value in self.morse_code.items():
                    if value == i:
                        res += key
            else:
                pass


        return res


    def _logic(self):
        print('Welcome to MorseDecoder\nchose command')
        print('1: text to morse')
        print('2: morse to text')
        user_choise = input()
        result = ''
        if user_choise == '1':
            print('Enter text to code:')
            message = str(input())
            result = self.toMorse(message)
        elif user_choise == '2':
            print('Enter code to converting:')
            code_message = str(input())
            result = self.toText(code_message)
        else:
            print('Ooops, no such command as' + str(user_choise))
        return result


    def main(self):
        return self._logic()


if __name__ == '__main__':
    x = Morse()

    res = x.main()
    print(res)
    # x.toText()
