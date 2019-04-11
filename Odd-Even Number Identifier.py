import random
from colorama import Fore
from colorama import init

# initialize colorama to work
init()

print ("                        ")
print (Fore.RED + "Welcome to odd-even number identifier !      ~Anonymous")
print (Fore.CYAN + "-------------------------------------------------------")
print ("                        ")

# system generated value (Secure)
secure_random = random.SystemRandom()

# printing new replies with every new output
even_replies = ["Even Number", "It's an even number !", "Yaay ! An even number"]
odd_replies = ["Odd Number", "It's an odd number !", "Yaay ! An odd number"]

while True:
    try:

        def odd_or_even():

            Fore.MAGENTA
            number = float(input("Enter A Number : "))

            if number % 2 == 0: # criteria for even numbers
                print(Fore.BLUE + secure_random.choice(even_replies))
                print("                        ")
            else:
                print(Fore.GREEN + secure_random.choice(odd_replies))
                print("                        ")

        odd_or_even()

    except ValueError: # null or incorrect input

        print ("Oops! An error occured... Please try again...")
        print ("                        ")