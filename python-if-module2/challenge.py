input = input('Would you like to continue? ')

if input == 'n' or input == "no":
    print("Exiting")
elif input == 'y' or input == "yes":
    print("Continuing...")
    print("Complete!")
else:
    print("Please try again and respond with yes or no.")