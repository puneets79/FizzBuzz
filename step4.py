def calc (operator, number_1, number_2):
    answer = 0;
    if operator == "+":
        answer = int(number_1) + int(number_2)
    elif operator == "-":
        answer = int(number_1) - int(number_2)
    elif operator == "x":
        answer = int(number_1) * int(number_2)
    elif operator == "/":
        answer = int(number_1) / int(number_2)
    return answer

with open("step4.txt",'r') as f:
    text_string = f.read().splitlines()

instructions = []
i=0
while i < len(text_string):
    mystring = text_string[i].split(' ')
    if text_string[i] in instructions:
        break
    else:
        instructions.append(text_string[i])
    if mystring[0] == 'goto':
        if (mystring [1] == 'calc'):
            i = int(calc(mystring[2],mystring[3],mystring[4]))
        else:
            i = int(mystring[1]);
        i -= 1
    elif mystring[0] == 'remove':
        removed = text_string.pop(int(mystring[1])-1)
        print (removed)
        i += 1
    elif mystring [0] == 'replace':
        text_string[int(mystring[1]) -1 ] = text_string[int(mystring[1]) - 1]
        i+=1

print ('final instruction is  ' + text_string[i] + ' on line number ' + str(i+1))


