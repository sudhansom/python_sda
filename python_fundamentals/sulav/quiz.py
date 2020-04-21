import time

print("*****HELLO AND WELCOME TO THE MATHS QUIZ!*****")
time.sleep(1)
name = input("What is your name?")  # welcomes the user
print("Well, good luck, " + name + ", and try your best!")
print("----------------------------------------------")
time.sleep(2)


def main():  # this helps restart the code, by indenting the lines of code you want to restart
    b = 0
    d = 1

    while b < 15:  # does the loop until b > 15
        import random
        x = random.randint(0, 100)
        y = random.randint(0, 100)  # imports random integers

        import operator

        op_mappings = {"+": operator.add, "-": operator.sub}  # imports random variables

        op = random.choice(["+", "-"])
        ans = op_mappings[op](x, y)
        c = int(input(str(d) + ") ""What is " + str(x) + op + str(y) + " ?"))
        if ans == c:  # I put statements when the answer is right/wrong
            print("CORRECT!")
            b = b + 1
            d = d + 1
        elif ans != c:
            print("INCORRECT!")
            time.sleep(1)
            print("The CORRECT answer is " + str(ans) + " !")
            time.sleep(1)
            print("Your score is " + str(b) + " /15 !")
            time.sleep(1)
            again = input("Would you like to restart? (yes/no)")
            if again == "yes":
                print("----------------------------------------------")
                print("    ____  ____________________    ____  ______")
                time.sleep(0.3)
                print("   / __ \/ ____/ ___/_  __/   |  / __ \/_  __/")
                time.sleep(0.3)
                print("  / /_/ / __/  \__ \ / / / /| | / /_/ / / /   ")
                time.sleep(0.3)
                print(" / _, _/ /___ ___/ // / / ___ |/ _, _/ / /   ")
                time.sleep(0.3)
                print("/_/ |_/_____//____//_/ /_/  |_/_/ |_| /_/    ")
                print("---------------------------------------------")
                main()  # goes back to def.main():

            else:
                print("Ok then, goodbye!")
                exit()  # stops the code

    print("██╗    ██╗███████╗██╗     ██╗         ██████╗  ██████╗ ███╗   ██╗███████╗    ██╗")
    time.sleep(0.3)
    print("██║    ██║██╔════╝██║     ██║         ██╔══██╗██╔═══██╗████╗  ██║██╔════╝    ██║")
    time.sleep(0.3)
    print("██║ █╗ ██║█████╗  ██║     ██║         ██║  ██║██║   ██║██╔██╗ ██║█████╗      ██║")
    time.sleep(0.3)
    print("██║███╗██║██╔══╝  ██║     ██║         ██║  ██║██║   ██║██║╚██╗██║██╔══╝      ╚═╝")
    time.sleep(0.3)
    print("╚███╔███╔╝███████╗███████╗███████╗    ██████╔╝╚██████╔╝██║ ╚████║███████╗    ██╗")
    time.sleep(0.3)
    print(" ╚══╝╚══╝ ╚══════╝╚══════╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚═╝")
    time.sleep(1)
    again = input("Would you like to continue? (yes/no)")
    if again == "yes":
        main()
    else:
        print("Goodbye!")
        exit()
main() #this is where you want your repeated code to stop