

def placeOrder():
    prices = {
    1:("bag of laundry" , 5.00),
    2:("dry clean shirt" , 4.00),
    3:("dry clean pants" , 8.00),
    4:("dry clean dress" , 12.00),
    5:("dry clean suit" , 15.00)}

    print("Please choose from the following list of services:")

    for k, v in prices.items():
        print('{}) {}: ${:.2f}'.format (k, v[0], v[1]))

    customer_list = []

    keep_choosing = 'Y'
    while keep_choosing == 'Y':
        choice = int(input("\nEnter your selection: "))

        if choice in prices.keys():
            customer_list.append((prices[choice][0], prices[choice][1]))
        else:
            print('Invalid Choice')
        
        keep_choosing = input('Would you like to add any additional services? (Y/N): ').upper()
    

    total = 0
    for i in customer_list:
        total += (i[1])
    file = open("receipt.txt", 'w')

    file.write("\t\t------------------RECEIPT-----------------------\n")
    for i in customer_list:   
        file.write("\t\t{}\t{:.2f}\n".format(i[0], i[1]))
    file.write("\n\t\tTOTAL: \t${:.2f}".format(total))
    
    file.close()