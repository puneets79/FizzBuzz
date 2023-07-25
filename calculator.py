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
    elif operator == "^":
        answer = int(number_1) ** int(number_2)
    return answer

with open("my_file.txt",'r') as f:
    text_string = f.read().splitlines()

final_calc = 0
for line in text_string:
    mystring = line.split(' ')
    calculation = calc(mystring[1],mystring[2],mystring[3])
    print(calculation)
    final_calc += calculation

print ('final calculation is ' + str(final_calc))


