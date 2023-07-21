for number in range(1,100):
    text = ""
    if (number % 11) == 0:
        text += "Bong"
    if (number % 7 == 0):
        text += "Bang"
    if (number % 5 == 0):
        text += "Buzz"
    if (number % 3 == 0):
        text += "Fizz"
    if (text == ""):
        text = str(number)
    print (text)
