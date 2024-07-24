import read
import write
from datetime import datetime

def for_portal(user):
    """This function is to determine whether the input from user is valid and
    make to run through different fuction according to the need of the user"""
    while user>3 or user <=0:
        print("Only integer and only value upto 3 is accepted")
        user=int(input("Enter the required number : "))
        
    if user ==1:
        for_selling_laptop()
    elif user == 2:
        for_buying_laptop()
    else:
        print("thank you!! for using the portal")

    


def for_selling_laptop():
    """This function is to sale the available laptop from the file and update the existing file after showing to 
    the user about the bills which were selected by the user"""
    C_name= input("enter your name: ")
    phone_number=int(input("enter your phone number: "))
    selling=[]
    print("\n")
    print("---------------------------------------------------------------------------------------------")
    print("|S.N.|Laptop Name\t | Company name  |Price \t | Quant | Processor \t | Graphics \t")
    print("---------------------------------------------------------------------------------------------")

    read.laptop_file_display()#importing function from read.py
    product_list= read.laptop_portal()#importing and storing the return value of laptop_portal to product_list
    
    valid_id =int(input("please provide the ID of the laptop you want to book"))
    while valid_id <= 0 or valid_id > len(product_list):
        print("please provide a valid laptop id")

        print("\n")
        valid_id =int(input("please provide the ID of the laptop you want to book"))

    user_quantity=int(input("please provide the required quatity"))
    print("\n")

    get_quantity_of_selected_laptop =product_list[valid_id][3]
    while user_quantity <= 0 or user_quantity > int(get_quantity_of_selected_laptop):
        print("Dear customer, the quantity looking is not available")
        print("\n")

        user_quantity =int(input("Please provide another quantity requirement:"))
            
        print("\n")
            
         #restocking the text file
    product_list[valid_id][3]=int(product_list[valid_id][3])-int(user_quantity)
        

        #write.adding_sales_to_file()
    file =open("laptop.txt","w")
    for values in product_list.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close()

    #storing in new list 
    nameoflaptop= product_list[valid_id][0]
    numberoflaptop= user_quantity
    priceoflaptop=product_list[valid_id][2].replace("$",'')
    totalprice= int(priceoflaptop) * int(user_quantity)

    selling.append([nameoflaptop,numberoflaptop,priceoflaptop,totalprice])
    
    again_user = str(input("enter if you want to continue?(n/y): ")).lower()
    while again_user != "y" and again_user != "n":
        print("Type only y for yes and n for no")

        again_user = str(input("enter if you want to continue?(n/y): ")).lower()
    if again_user == "y":
        user_continue= True
        while user_continue == True:
            print("\n")
            print("---------------------------------------------------------------------------------------------")
            print("|S.N.|Laptop Name\t | Company name  |Price \t | Quant | Processor \t | Graphics \t")
            print("---------------------------------------------------------------------------------------------")

            read.laptop_file_display()
            product_list= read.laptop_portal()
            
            valid_id =int(input("please provide the ID of the laptop you want to book"))
            while valid_id <= 0 or valid_id > len(product_list):
                print("please provide a valid laptop id")

                print("\n")
                valid_id =int(input("please provide the ID of the laptop you want to book"))

            user_quantity=int(input("please provide the required quatity"))
            print("\n")

            get_quantity_of_selected_laptop =product_list[valid_id][3]
            while user_quantity <= 0 or user_quantity > int(get_quantity_of_selected_laptop):
                print("Dear customer, the quantity looking is not available")
                print("\n")

                user_quantity =int(input("Please provide another quantity requirement:"))
                    
                print("\n")
                    
                #restocking the text file
            product_list[valid_id][3]=int(product_list[valid_id][3])-int(user_quantity)
                

                #adding sales to file
            file =open("laptop.txt","w")
            for values in product_list.values():
                file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
                file.write("\n")
            file.close()

            nameoflaptop= product_list[valid_id][0]
            numberoflaptop= user_quantity
            priceoflaptop=product_list[valid_id][2].replace("$",'')
            totalprice= int(priceoflaptop) * int(user_quantity)

            selling.append([nameoflaptop,numberoflaptop,priceoflaptop,totalprice])

            again_user = input("enter if you want to continue?(n/y): ").lower()
            while again_user != "y" and again_user != "n":
                print("Type only y for yes and n for no")

                again_user = input("enter if you want to continue?(n/y): ").lower()

            if again_user == "y":
                user_continue= True
            else:
                cost_of_shipping=0
                price=0
                shipping_cost= input("Is shipping needed(y/n): ").lower()
                while again_user != "y" and again_user != "n":
                    print("Type only y for yes and n for no")

                    shipping_cost= input("Is shipping needed(y/n): ").lower()
                if shipping_cost == "y":
                    cost_of_shipping= 500
                
                for each in selling:
                    price += int(each[3])
                    
                vat_amount = ((13/100)*price)+ price
                grand_balance = vat_amount + cost_of_shipping

                date_time= datetime.now()
                second=str(datetime.now().second)
                year=str(datetime.now().minute)
                time=str(year)+str(second)
                for_print_bill(C_name,phone_number,date_time,selling,price,vat_amount,cost_of_shipping,grand_balance)

                write.for_storing_sales(C_name,phone_number,date_time,selling,price,vat_amount,cost_of_shipping,grand_balance,time)
                break
            
    else:
        #bill generating
        cost_of_shipping=0
        price=0
        shipping_cost= input("Is shipping needed(y/n): ").lower()
        while again_user != "y" and again_user != "n":
            print("Type only y for yes and n for no")

            shipping_cost= input("Is shipping needed(y/n): ").lower()
        if shipping_cost == "y":
            cost_of_shipping= 500
        
        for each in selling:
            price += int(each[3])
            
        vat_amount = ((13/100)*price)+ price
        grand_balance = vat_amount + cost_of_shipping

        date_time= datetime.now()
        second=str(datetime.now().second)
        year=str(datetime.now().minute)
        time=str(year)+str(second)
        
        for_print_bill(C_name,phone_number,date_time,selling,price,vat_amount,cost_of_shipping,grand_balance)

        write.for_storing_sales(C_name,phone_number,date_time,selling,price,vat_amount,cost_of_shipping,grand_balance,time)
        
    return selling


#for adding the laptops to the store 
def for_buying_laptop():
    """This function is to increase the stock of laptops as this fuction purchase from the manufacture
    to those laptops available in the shop"""
    buying=[]
    emp_name =input("Enter the emloyee name : ")

    print("\n")
    print("---------------------------------------------------------------------------------------------")
    print("|S.N.|Laptop Name\t | Company name  |Price \t | Quant | Graphics \t | RAM \t")
    print("---------------------------------------------------------------------------------------------")
    
    read.laptop_file_display()
    product_list= read.laptop_portal()
    #print(product_list)

    purchase_id= int(input("Enter the desired Id of product to be added in the store: "))
    while purchase_id > len(product_list) or purchase_id <=0 :
        print("The above deal cannot be carried. Please provide the ID from the above")
        purchase_id= int(input("Enter the desired Id of product to be added in the store: "))
        print("\n")

    purchasing_num=int(input("Enter the required number of laptops : "))
    while purchasing_num <=0:
        print("Please provide the quantity needed to be add in the store: ")
        purchasing_num=int(input("Enter the required number of laptops : "))
        print("\n")

            #restocking the text file
            
    product_list[purchase_id][3]= int(product_list[purchase_id][3])+int(purchasing_num)
        #write.adding_sales_to_file()
    file =open("laptop.txt","w")
    for values in product_list.values():
        file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
        file.write("\n")
    file.close()

    nameoflaptop= product_list[purchase_id][0]
    numberoflaptop= purchasing_num
    priceoflaptop=product_list[purchase_id][2].replace("$",'')
    totalprice= int(priceoflaptop) * int(purchasing_num)

    buying.append([nameoflaptop,numberoflaptop,priceoflaptop,totalprice])

    again_purchase=input("Would you like to add more of laptops to the store(Y/N)?: ").lower()
    while again_purchase!= "y" and again_purchase!= "n":
        print("Only type:- y for yes and n for no")
        print("\n")
        again_purchase=input("Please type y for yes and n for no(Y/N)?: ").lower()

    if again_purchase=="y":
        user_continue = True
        while user_continue == True:
            print("\n")
            print("---------------------------------------------------------------------------------------------")
            print("|S.N.|Laptop Name\t | Company name  |Price \t | Quant | Graphics \t | RAM \t")
            print("---------------------------------------------------------------------------------------------")
                
            read.laptop_file_display()
            product_list= read.laptop_portal()
            #print(product_list)

            purchase_id= int(input("Enter the desired Id of product to be added in the store: "))
            while purchase_id > len(product_list) or purchase_id <=0 :
                print("The above deal cannot be carried. Please provide the ID from the above")
                purchase_id= int(input("Enter the desired Id of product to be added in the store: "))
                print("\n")

            purchasing_num=int(input("Enter the required number of laptops : "))
            while purchasing_num <=0:
                print("Please provide the quantity needed to be add in the store: ")
                purchasing_num=int(input("Enter the required number of laptops : "))
                print("\n")

                        #restocking the text file
                        
            product_list[purchase_id][3]= int(product_list[purchase_id][3])+int(purchasing_num)
            
            file =open("laptop.txt","w")
            for values in product_list.values():
                file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
                file.write("\n")
            file.close()

            nameoflaptop= product_list[purchase_id][0]
            numberoflaptop= purchasing_num
            priceoflaptop=product_list[purchase_id][2].replace("$",'')
            totalprice= int(priceoflaptop) * int(purchasing_num)
            buying.append([nameoflaptop,numberoflaptop,priceoflaptop,totalprice])

            again_purchase=input("Would you like to add more of laptops to the store(Y/N)?: ").lower()
            while again_purchase!= "y" and again_purchase!= "n":
                print("Only type:- y for yes and n for no")
                print("\n")
                again_purchase=input("Please type y for yes and n for no(Y/N)?: ").lower()
                
            if again_purchase== "y":
                user_continue= True
            else:
                tprice=0
                for each in buying:
                    tprice += int(each[3])
                vat_amount = ((13/100)*tprice)
                grand_balance = tprice + vat_amount

                date_time= datetime.now()
                second=str(datetime.now().second)
                year=str(datetime.now().minute)
                easy=str(year)+str(second)
            

                for_print_buy(emp_name,date_time,buying,tprice,vat_amount,grand_balance)

                write.for_purchasing_laptops(emp_name,date_time,buying,tprice,vat_amount,grand_balance,easy)
                break
    else:
        tprice=0
        for each in buying:
            tprice += int(each[3])
        vat_amount = ((13/100)*tprice)
        grand_balance = tprice + vat_amount

        date_time= datetime.now()
        second=str(datetime.now().second)
        year=str(datetime.now().minute)
        easy=str(year)+str(second)

        for_print_buy(emp_name,date_time,buying,tprice,vat_amount,grand_balance)

        write.for_purchasing_laptops(emp_name,date_time,buying,tprice,vat_amount,grand_balance,easy)
    return buying

def for_print_bill(name,ph,date,sells,total,vat,ship,grand):
    """This function is to show bill in the shell of the platform used by the user"""
    print("\n")
    print("___________________________________________________________________")
    print("\t \t \t|| OLIZ LAPTOP STORE ||")
    print("\t \t || Kathmandu-12,Kamaladi(Rising Mall) ||")
    print("\t \t || Phone number: 9867212227,974345494 ||")
    print("\n")
    print("Bill no: ",date)
    print("Address: ----")
    print("Pan no: 611120614")
    print("Customer name:",name)
    print("Phone Number",ph)
    print("Payment mode: cash only")
    print("___________________________________________________________________")
    print("-------------------------------------------------------------------")
    
    print("SN Product Name \t Qty \t Rate \t Amount")
    print("-------------------------------------------------------------------")
    
    a=1
    for i in sells:
        print(a, i[0], "\t \t " ,i[1], "\t " ,i[2], "\t " ,"$", i[3])
        a=a+1
    
    print("\n")
    print("--------------------------------------------------------------------")
    print("\t \t \t \t Gross Amount: $"+str(total))
    print("\t \t \t \t Discount: unavailable")
    print("\t \t \t \t Amount After VAT: "+str(vat))
    print("\t \t \t \t Shipping cost: $"+str(ship))
    print("\t \t \t \t Net Amount : $"+str(grand))
    print("--------------------------------------------------------------------")
    print("\t \t WELCOME TO GREAT SHOPPING EXPERIENCE")
    print("\t \t EXCHANGE IN 7 DAYS WITH INVOICE")
    print("\t \t \t ---CONDITION APPLY---")
    print("--------------------------------------------------------------------")
    print("--------------------------------------------------------------------")
    print("\t \t \t *** HAVE A GOOD DAY ***")
    print(" \t \t **** THANK YOU FOR SHOPPING WITH US ****")
    print("___________________________________________________________________")
    print("\n")



def for_print_buy(name,date,buys,total,vat,grand):
    """This function is to show purchase history from the manufacture to the employee"""
    print("_________________________________________________________")
    print("-------------------------------------------------------------------")
    print("Stock was manuplated by :",name)
    print("Buying_bill : ",date)
    print("SN Product Name \t Qty \t Rate \t Amount")
    print("-------------------------------------------------------------------")
    
    a=1
    for i in buys:
        print(a, i[0], "\t \t " ,i[1], "\t " ,i[2], "\t " ,"$", i[3])
        a=a+1
    
    print("\n")
    print("--------------------------------------------------------------------")
    print("\t \t \t \t Gross Amount: $",str(total))
    print("\t \t \t \t Discount: unavailable")
    print("\t \t \t \t  VAT amount: "+str(vat))
    
    print("\t \t \t \t Total Amount : $",grand)
    print("--------------------------------------------------------------------")
