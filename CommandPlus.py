import time
import os
print("Welcome to CommandPlus Application")
def MainOfApp():
    while True:
        user = input("Type Command: ")
        if user == "help":
            helplist = ["1)Calculator", "2)Games Downloader", "3)Apps Downloader", "4)Settings"]
            for hlist in helplist:
                print(hlist)
        elif user == "1":
            print("")
            print("")
            print("------------------")
            print("")
            print("Open Calculator...")
            print("")
            print("------------------")
            print("")
            print("")
            time.sleep(5)
            Calculator()
            break
        elif user == "cpver":
            print("-----------------------------")
            print("")
            print("CommandPlus 1.0.1")
            print("")
            print("-----------------------------")
            print("")
            print("This Application By GigaCoder")
            print("")
            print("-----------------------------")
            time.sleep(5)
        elif user == "3":
            print("Opening Apps Downloader...")
            print("")
            time.sleep(6.5)
            Apps_Downloader()
            break
def Calculator():
    while True:
        user = input("Type Command: ")
        if user == "help":
            helplist = ["1)Back", "2)Start The Calculator"]
            for i in helplist:
                print(i)
        elif user == "2":
            num1 = float(input("First Number: "))
            operator = str(input("Operator: "))
            num2 = float(input("Second Number: "))
            #System
            if operator == "+":
                print(num1, "+", num2, "=", num1 + num2)
            elif operator == "-":
                print(num1, "-", num2, "=", num1 - num2)
            elif operator == "*":
                print(num1, "*", num2, "=", num1 * num2)
            elif operator == "/":
                print(num1, "/", num2, "=", num1 / num2)
            elif operator == "**":
                print(num1, "**", num2, "=", num1 ** num2)
        elif user == "1":
            print("--------------------------")
            print("")
            print("Retune To The Main Menu...")
            print("")
            print("--------------------------")
            time.sleep(4)
            MainOfApp()
            break
def Apps_Downloader():
    while True:
        user = input("Type Command: ")
        if user == "help":
            listh = ["1)Browsers", "2)Audio Apps", "3)Cracked Apps"]
            for i in listh:
                print(i)
        elif user == "1":
            print("All Browsers Available:")
            print("")
            print("")
            print("1)Chrome")
            print("2)FireFox")
            print("3)Brave")
            print("4)Microsoft Edge")
            print("")
            print("")
            installuser = input("Select The Browser: ")
            if installuser == "1":
                print("--------------------")
                print("")
                print("Installing Chrome...")
                print("")
                print("--------------------")
                os.startfile('D:\Dev\PythonProjects\RealApps\CommandPlus (1.0.1)\Installer\AppsInstall\Browsers\Chrome\ChromeSetup.exe')
                time.sleep(60)
                print("--------------------------")
                print("")
                print("Retune To The Main Menu...")
                print("")
                print("--------------------------")
                MainOfApp()
                break
            

MainOfApp()
