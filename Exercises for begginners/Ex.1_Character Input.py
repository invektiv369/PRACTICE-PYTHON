##Create a program that asks the user to enter their name and their age. 
##Print out a message addressed to them that tells them the year that they will turn 100 years old.
##Створіть програму, яка просить користувача ввести своє ім’я та вік. 
##Роздрукуйте повідомлення, адресоване їм, із зазначенням року, коли їм виповниться 100 років.
name = input("What is your name: ")
age = int(input("How old are you: "))
year = 2023 - age + 100
print(name + ", you will be 100 years old in the year " + str(year))