import os

from kahoot import client
import random
from colorama import Fore, Back, Style 

os.system('color')


bot = client()

def spambots():
    gameid = input(f"{Style.BRIGHT}{Fore.RED}[{Fore.WHITE}?{Fore.RED}]{Fore.RESET}Enter the game pin {Fore.RED}>{Fore.RESET} ")
    botamount = input(f"{Style.BRIGHT}{Fore.RED}[{Fore.WHITE}?{Fore.RED}]{Fore.RESET}Enter the amount of bots (max 2000) {Fore.RED}>{Fore.RESET} ")
    custom_username = input(f"{Style.BRIGHT}{Fore.RED}[{Fore.WHITE}?{Fore.RED}]{Fore.RESET}Enter the name of the bot{Fore.RED}>{Fore.RESET} ")

    def joingame():
        username = (custom_username + str(random.randint(1, 10000)))
        bot.join((gameid), username)

        def joinHandle():
            pass

        bot.on("joined", joinHandle)
        print(f"{Style.BRIGHT}{Fore.GREEN}Joined game"+gameid+f"with username{Fore.WHITE}"+username+".")

    for x in range(0, (int(botamount))):  # + 10  this is not code
        joingame()
spambots()