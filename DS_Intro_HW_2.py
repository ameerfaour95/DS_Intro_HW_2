#Ameer Faour 316540467
#Q.1
def reverse(sentence, reverse_word):
    if type(reverse_word) is not str:
        return 'invalid input'
    else:
        x=sentence.split()
        rev='The word was not found'
        for i in x:
            if i==reverse_word:
                rev=i[::-1]
                break
            else:
                continue
        return rev
#----------------------------------------
#Q.2:
def compute_equation(equation):
    powerOff=0
    result=0
    for e in equation:
        if e not in ['1','2','3','4','5','6','7','8','9','0'] and e not in ['*','/','-','+','**','.']:
            powerOff = 1
            return 'invalid input detected'
            break
        else:
            powerOn=1
    if powerOn==1 and powerOff==0:
        result=eval(equation)
        if str(result)[-1]=='0':
            return int(result)
        else:
            return result



