import random

target = random.randint(1, 5)
# print(target)
count = 0

typed_number = input("Guess a number between 1 and 5: ")
count += 1

while typed_number == '' or not(typed_number.isnumeric()) or int(typed_number) != target:
    typed_number = input("Guess a number between 1 and 5: ")
    count += 1

print("You guessed it in " + str(count) + " tries!")