from email_validator import validate_email, EmailNotValidError
import io,os,arg
from colorama import Fore,Back,Style
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print(Style.RESET_ALL)
try:
    maillist = io.open("input.txt", mode="r", encoding="utf-8")
    content = maillist.readlines()
    maillist.close()

    file1 = open("valid.txt", "w+")
    file2 = open("invalid.txt", "w+")

except:
    print("FILE ERROR - Please check the files , in the directory it should be only input.txt")



frequency = 2500  # Set Frequency To 2500 Hertz
duration = 200  # Set Duration To 1000 ms == 1 second
while (True):
    cls()

    choice = input(Back.GREEN+"Tim & Tro e-mail validator \n"
                   +Back.BLACK+Fore.WHITE+ "The program will read the list from INPUT.TXT,You can check the list with two modes:\n\n"+Back.WHITE+Fore.BLACK+
          "1. "+Back.BLUE+Fore.WHITE+"active-mode "+Back.WHITE+Fore.BLACK+" will check if the mail domain really exist and is accessible ( more accurate but Takes more time )\n"
          "2. "+Back.BLUE+Fore.WHITE+"passive-mode"+Back.WHITE+Fore.BLACK+" will only check the mail structure ( fast ) \n\n"+Back.YELLOW+Fore.BLACK+
          "Enter 1 for active-mode and 2 for passive-mode:\n"+Style.RESET_ALL)
    print(Style.RESET_ALL)
    if choice == '1':
        USERSET = True
        break
    else:
        if choice =='2':
            USERSET = False
            break
        else:
            continue

cls()
#os.system("color A")



i=0
print("Processing...please wait...")
for item in content:
        i +=1
        item = str(item)

        item = item.replace("www.","")
        item = item.replace("WWW.","")
        item = item.replace("Www.","")

        item = item.replace("\n", '')
        print(Style.RESET_ALL)

        try:

            v = validate_email(item ,check_deliverability=USERSET) # validate and get info
            item = v["email"] # replace with normalized form


            print(Fore.WHITE+"no "+str(i)+" "+Back.GREEN+Fore.BLACK+item +Fore.YELLOW+Back.BLACK+" is valid")
            item = item + "\n"
            file1.write(str(item))

        except EmailNotValidError as e:
            # email is not valid, exception message is human-readable
            print(Fore.WHITE+"no "+str(i)+" "+Back.RED+Fore.BLACK+item+" "+Fore.RED+Back.BLACK+str(e))
            invalid_mail = str(item) + " >> RESULT >> " + str(e) + "\n"
            file2.write(invalid_mail)


file1.close()
file2.close()
print(Style.RESET_ALL)
print("DONE!")