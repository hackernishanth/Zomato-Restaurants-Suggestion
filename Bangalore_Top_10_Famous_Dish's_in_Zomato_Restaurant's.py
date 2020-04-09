# Problem Statement 
# suggestion to taste the Zomato restaurant near you
# Required Packages for Data Analysis
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Loading the dataset for giving the suggestion
Input_data = pd.read_csv("/home/nishanth_kumar_27_11/Videos/dog vs cat/zomato-bangalore-restaurants/zomato.csv")
print(Input_data.head())

# Problem Statement
# To find the dish that are famous for banglore depends upon the dataset
dish_liked = []
# Finding the length of the dataset
length_of_dataset = len(Input_data["dish_liked"])
print(length_of_dataset)
# Separating the Dish from dataset column dish_like 
for data in range (length_of_dataset) :
    try:
        temp = Input_data["dish_liked"][data]
        dish_liked.append(temp.split(","))
        #data = data + 1
        
    except:
        pass
print(len(dish_liked))# It is in 2D array    
# print(dish_liked)

# Separaed dish are save in an 1D array    
permanent_storage = []
famous_dish = []
for i in dish_liked :
    words = i[0]
    permanent_storage.append(words)

    
#the conveted 1d saved as below
print(len(permanent_storage))
#print(permanent_storage)


# The dish that are not repeated are
p = []
p.append(list(dict.fromkeys(permanent_storage)))
print(len(p[0]))
#print(p)
     
players_details, players_name = [], []
for each_player in permanent_storage:
    if not(each_player in players_name):
        players_name = players_name + [each_player]
        players_details = players_details + [[each_player, 1]]
    else:
        for index in range(len(players_details)):
            if players_details[index][0] == each_player:
                players_details[index][1] = players_details[index][1]+1
famous_dish_available = []
dish_available = []
for each in players_details:
    famous_dish_available.append(each[0])
    dish_available.append(each[1])
    #break
    print ('{} : {}'.format(*each))
    #print(each)
#print(famous_dish_available)
#print(dish_available)

# Finding the Top 10 product's famous in Banglore
def insertionSort(arr): 
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)):
        key = arr[i] 
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key > arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key   
# Driver code to test above 
insertionSort(dish_available) 

for i in range (0,len(dish_available)): 
    print(dish_available[i]) 
    
    
_dish_available = []
for i in range (0,10): 
    _dish_available.append(dish_available[i])
print(_dish_available)
#print(famous_dish_available[0])


index = -1
finded_dish = []
for i in _dish_available:
    
    for each in  players_details:
            #print(each[1])
            index = index + 1
            #print(index)
            #break
            #print ('{} : {}'.format(*each))
            if each[1] == i : 
                #print(each[1])
                #print(i)
                finded_dish.append(famous_dish_available[index])
                print(famous_dish_available[index])
                break
    index = -1           
print(finded_dish)
print(_dish_available)



# x axis values 
x = finded_dish
# corresponding y axis values 
y = _dish_available


fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
    
# plotting the points  
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
         marker='o', markerfacecolor='blue', markersize=12, label='Price') 


for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('Dish that has been salesed highly...!') 
  
# function to show the plot 
plt.show() 
