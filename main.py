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
        }


    def toMorse(self, message):
        res_lst = list()
        for i in str(message):
            if i == ' ' or i == '  ':
                res_lst.append(i)
            elif str(i.upper()) in self.morse_code.keys():
                res_lst.append(self.morse_code.get(str(i.upper())))
            else:
                res_lst.append('~')
        
        return res_lst


    def toText(self, code):
        pass


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
            pass
        else:
            print('Ooops, no such command as' + str(user_choise))
        return result


    def main(self):
        result = ''
        result_list = self._logic()
        for i in result_list:
            result += i
        return result


if __name__ == '__main__':
    x = Morse()

    res = x.main()
    print(res)
    # x.toText()
