##Create a program that asks the user to enter their name and their age. 
##Print out a message addressed to them that tells them the year that they will turn 100 years old.
##Створіть програму, яка просить користувача ввести своє ім’я та вік. 
##Роздрукуйте повідомлення, адресоване їм, із зазначенням року, коли їм виповниться 100 років.
language = int(input("EN(1)/UA(2):"))
if language == 1:
    name = input("What is your name: ")
    age = int(input("How old are you: "))
    year = 2023 - age + 100
    print(name + ", you will be 100 years old in the year " + str(year))
else:
    name = input("Як тебе звати?: ")
    age = int(input("Скільки тобі років?: "))
    year = 2023 - age + 100
    print(name + ", тобі буде 100 років у " + str(year) + " році")