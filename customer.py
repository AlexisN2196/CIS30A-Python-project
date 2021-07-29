import prices

def menuChoice(entry):
    if entry == '1':
        howWorks()
    elif entry == '2':
        seePrice()
    elif entry == '3':
        prices.placeOrder()
        set_date()
        print_receipt()
    else:
        print("That is not a valid entry")
   

def howWorks():
    #explain how it works read in from file
    explain = open("process.txt", "r")
    print(explain.read())
    explain.close()
    

def seePrice():
    #ouput services list from file
    services = open("services_list.txt", "r")
    print(services.read())
    services.close()


def set_date():
    #allow user to input date
    print("Enter the date you'd like us to drop off your bags, we'll retunr the following day for pick-up:")
    date = "none"
    while date.isnumeric() == False:
        date = input("Please enter a 2 digit day, month, and year (mm/dd/yy): ")
    
    rec = open("receipt.txt", 'a')
    rec.write("\nScheduled date: ("+ date+ ")")
    rec.close()

def print_receipt():
    print("\nHere is your receipt:\n")
    rec = open("receipt.txt", 'r')
    print(rec.read())
    rec.close()