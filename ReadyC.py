import os
import requests
from time import sleep

def main():

    os.system('cls & title Fluzy DLL ( Connecting ...)')

    print(" ")

    print("Check last version ...")

    auth_c = requests.get("https://pastebin.com/raw/jtGPSUX4").text

    if auth_c == "1":

        sleep(1)

        print(" ")

        print("Your dll is ready to use !")

        print(" ")

        sleep(1)

        print("Wait for Full release to use !")

        print(" ")

        sleep(1)

        exit = input("Do you want Beta Program ? ( Yes / No ) > ")

        if exit == "Yes":

            sleep(1)

            os.system('cls')

            print(" ")

            print("Dm developer to use Beta function !")

            print(" ")

    elif auth_c == "2":

        print(" ")

        print("New version out now update it !")

main()