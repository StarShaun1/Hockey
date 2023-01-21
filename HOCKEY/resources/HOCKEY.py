from colorama import Fore, Back, Style, init
from time import sleep
import os

init(convert=True)

print("Hello, welcome to HOCKEY.")

sleep(3)
def ques():
    haha = input(Fore.GREEN + "What Hockey team do you like? (t/m) : ")
    
    if haha == "m":
        print("you chose " + Fore.RED + "Montreal Canadiens.")
        sleep(4)
        os.system('cls')
        print(Fore.GREEN + "GOOD ENDING")
    else:
        if haha == "t":
            print("you chose " + Fore.BLUE + "Toronto Maple Leafs.")
            sleep(4)
            os.system('cls')
            print(Fore.RED + "#     # ####### #     #    ######  ### #######  #####  #     # ")
            print(Fore.RED + " #   #  #     # #     #    #     #  #     #    #     # #     # ")
            print(Fore.RED + "  # #   #     # #     #    #     #  #     #    #       #     # ")
            print(Fore.RED + "   #    #     # #     #    ######   #     #    #       ####### ")
            print(Fore.RED + "   #    #     # #     #    #     #  #     #    #       #     # ")
            print(Fore.RED + "   #    #     # #     #    #     #  #     #    #     # #     # ")
            print(Fore.RED + "   #    #######  #####     ######  ###    #     #####  #     # ")
        else:
            print(Fore.GREEN + "I didn't understand that. Try again.")
            sleep(4)
            ques()
ques()