from operator import contains

import numpy as np
import pandas as pd
import requests

# contact_book = dict()
contact_name = []
contact_number = []

while True:
    print("""
    1) Enter Contact
    2) Exit
    3) Search Contact
    4) Print All names and Contacts
    5) Export Contacts
    """)
    option  = int(input("Enter Option number:  "))
    if option == 1:
        rec_contact_name = input("Enter Contact Name: ")
        if rec_contact_name in contact_name:
            print("contact Name already existed")
        else:
            contact_name.append(rec_contact_name)
            rec_contact_number = int(input("Enter Contact Number:  "))
            contact_number.append(rec_contact_number)
            contacts  = list(zip(contact_name,contact_number))
    elif option ==2:
        exit()
    elif option ==3:
        if len(contact_name)!=0:
            input_search = input("Enter Name: ")
            for i in contacts:
                if i[0] == input_search:
                    print("Contact Name: {0}, Contanct Number: {1}".format(i[0],i[1]))
        else:
            print("The Contact Book is empty")
    elif option == 4:
        print("-------Contacts------------------")
        if len(contact_name)!=0:
            for i in contacts:
                print("Contact Name: {0}, Contanct Number: {1}".format(i[0],i[1]))
        else:
            print("The Contact Book is empty")
    elif option ==5:
        if len(contact_name) !=0:
            dict_contact = dict(zip(contact_name,contact_number))
            df = pd.DataFrame(data = list(dict_contact.items()),columns=['Name',"Number"])
            df.to_csv("C:/Users/User/Desktop/Jupyter Notebooks/Contacts.csv",index=False)

    # using zip function
    # contacts  = list(zip(contact_name,contact_number))


