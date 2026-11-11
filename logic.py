#guesses numbers 1-100 

#asks for user input number 1-100
number = int(input("pick a number 1-100 "))
while(0 > number or number > 100):
    print("try again, must be inside 1-100 range")
    number = int(input("pick a number 1-100 "))
#set two variables low and high to 1 and 100 first
low = 1
high = 99
#if inside range continue
while True:
    guess = ((low+high)//2)
    user = input((f"Is your number {guess}?(y/n) "))
    if user == "y":
        print("Yay!")
        break
    elif user == "n":
        hint = input("is it higher or lower?(h/l) ")
        if hint == "h":
            low = guess - 1
        elif hint == "l":
            high = guess + 1


    #guess ((low+high)/2)

#else try again