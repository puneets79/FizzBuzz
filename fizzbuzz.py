my_dict = {3:"Fizz",5:"Buzz",7:"Bang",11:"Bong",13:"Fezz",17:""}
input_text = input("max number ? ")
max_number = int(input_text)
for number in range(1,max_number):
    text = ""
    multiples = []
    if (number % 13) == 0:
        multiples.append(13)
    if (number % 11) == 0:
        multiples.append(11)
    if (number % 7 == 0):
        multiples.append(7)
    if (number % 5 == 0):
        multiples.append(5)
    if (number % 3 == 0):
        multiples.append(3)
    if (number % 17 == 0):
        multiples.append(17)
    if (multiples.count(17) > 0):
        multiples.sort(reverse=True)
    else:
        multiples.sort()
    
    if (len(multiples) == 0):
        text = str(number)
    else:
        for a_number in multiples:
            text+=my_dict[a_number]

    print (text)
