import customer
import prices

#main program menu 
print("*******************************************************")
print("                   WASH WONDERS                        ")
print("          your simple laundry solution                 ")
print("*******************************************************")
def mainMenu():
    print("\n                  MAIN MENU                          ")
    print("1. How it works")
    print("2. Prices")
    print("3. Place your order")


#loop will return to the main menu until user selects "n" to quit the program
keep_going = 'Y'
while keep_going != 'N' :
    mainMenu()
    entry = input("\nEnter your selection number: ")
    customer.menuChoice(entry)
    keep_going = input("\npress any key to continue or 'N' to quit: ").upper()

