# Problem Statement 
# suggestion to taste the Zomato restaurant near you
# Required Packages for Data Analysis
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Loading the dataset for giving the suggestion
Input_data = pd.read_csv("/home/nishanth_kumar_27_11/Videos/dog vs cat/zomato-bangalore-restaurants/zomato.csv")
print(Input_data.head())

# Getting the location of the person because we can use gps location in moblie phonr for this
place = input("Location :")

# displying the top 5 restaurant near you
index = 0
for loc in Input_data["location"] :
        #print(loc)
        if "Banashankari" == place :
            if "Banashankari" == loc :
                    index = index + 1
                    # we want only top 5 zomate restaurant near the customer
                    if index == 6 :
                        break                
                    print("\n"+"Suggested Zomato restaurant near you ")
                    # Displaying the special item in the restaurant
                    
                    count = 0
                    for rate in Input_data["rate"]:
                        _rate = []
                        # because the values are in 4.1/5 so i just speprate the rate and 5
                        r = rate.split('/')
                        _rate.append(r)
                        if count == 1 :
                            break
                        count = count + 1
                        # we are displaying the rating of the zomato restaurant 
                        print("Rating :"+" "+_rate[0][0])
                        vo = Input_data["votes"][index]
                        print("votes for the restaurant :",vo)
                        # Displaying type of restuarant
                        print("Type of restaurant:"+" "+Input_data["rest_type"][index])
                        
                        # We are checking for the booking the table to eat food in the restaurant
                        available = "Available"
                        unavailable = "Unavailable"
                        if "Yes" == Input_data["book_table"][index] :

                            print("Booking table :"+" "+available)
                            print("You can book the table using below link") 
                            
                        elif "No" == Input_data["book_table"][index]:
                            print("Booking table :"+" "+unavailable)
                                
                        if "Yes" == Input_data["online_order"][index] :
                            print("online order are:"+" "+available+"\n")
                                                              
                        elif "No" == Input_data["online_order"][index]:    
                            print("online order are:"+" "+unavailable+"\n")
                            
                        # Displaying the Famous dish like in that restaurant
                        print("Famous dish like in that restaurant :"+"\n"+"\t"+Input_data["dish_liked"][index]+"\n")        
                        
                        print("Price menu card :" +" "+Input_data["cuisines"][index])
                        print("cuisines approx_cost(for two people):" +" "+Input_data["approx_cost(for two people)"][index])
                        print("Name of the owner :"+" "+Input_data["name"][index])    
                        print("Contact Number :"+" "+Input_data["phone"][index])
                        
                                                              
                        # Displaying the Address of the particular zomato restaurant
                        address = Input_data["address"][index]
                        add = Input_data["address"][0]
                        _address = []
                        temp = []
                        for i in range (1):
                            a = add.split(',')
                            _address.append(a)
                            #print(_address[i])
                        print("Address :"+" ") 
                        # Displaying the contact number of the zomato restaurant
                        for i in range (len(_address[0])) :
                            print("\t"+_address[0][i].strip())
                        print("\n")
                        # Displying the top 2 review of the zomato restaurant 
                        for i in Input_data["reviews_list"] :
                            for j in range(5):
                                
                                a = (i.split(','))
                                print(a[j].split("\n"))
                            else:
                                break
                        # Displying the url for the zomato restaurant
                        print("To visit the website use below link :"+"\n"+Input_data["url"][index]+"\n") 
                    
        else:
                print("There is no Zomato reataurant near by you")
