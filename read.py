
#doc string is needed
#pring(laptop_portal.__doc.__) helps to print the doc string of the function


def laptop_portal():
    """This is for the accessing the laptop.txt file containing in the same folder/file of
the exact program existence"""
    file=open("laptop.txt","r")
    laptop_dictionary ={}
    laptop_id=1
    for line in file:
        line = line.replace("\n","")
        l= line.split(",")
        laptop_dictionary[laptop_id]=l
        laptop_id+= 1
    return laptop_dictionary


def laptop_file_display():
    """Making the file to display in the tabular form to take id of laptop from
the user and view the quantity"""
    file = open("laptop.txt","r")
    a=1
    for line in file:
        print("|",a," |"+line.replace(",","\t | "))
        a += 1
        print("---------------------------------------------------------------------------------------------")
        
    print("\n")
    print("\t**----------------------------*Products Above*--------------------------------------**")
    print("\n")
    
    file.close()
    
