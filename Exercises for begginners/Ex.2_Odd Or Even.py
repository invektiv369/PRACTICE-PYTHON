## Ask the user for a number.
## Depending on whether the number is even or odd, print out an appropriate message to the user.
## If the number is a multiple of 4, print out a different message.
## Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
## If check divides evenly into num, tell that to the user. 
## If not, print a different appropriate message.num = int(input("give me a number to check: "))

## Попросіть у користувача номер. 
## Залежно від того, парне чи непарне число, роздрукуйте відповідне повідомлення для користувача.
## Якщо число кратне 4, роздрукуйте інше повідомлення.
## Попросіть користувача ввести два числа: одне число для перевірки (назвіть його num) і одне число для поділу (перевірка). 
## Якщо перевірка ділиться рівномірно на num, повідомте про це користувачеві. 
## Якщо ні, надрукуйте інше відповідне повідомлення.

num = int(input("give me a number to check: "))
check = int(input("give me a number to divide by: "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)