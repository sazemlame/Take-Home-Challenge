"""
    Automated Parking System:

    This application helps you manage a parking lot of n slots. The program has the following functionalities:
    1. Park a car in empty slot and store the licence plate number and age of the driver
    2. Record which car has left the parking spot
    3. Search for the slot number for a particular licence number and age
    4. Search for licence plate details for drivers of same age


    A list of dictionaries containing details for each car has been implemented. A number of constraints have been taken into care like:
    1. The first line of file should create a parking lot
    2. Same car cannot be parked twice
    3. Driver cannot be under the age of 18
    4. The slot which is being vacated cannot be greater than the length of parking lot 


    
    """

import re
import sys


def car_park(y):
    # print("triggrting parking function")
    parking = {}
    parking["licence_plate_no"] = ""
    parking["age"] = ""
    for s in y.split():
        if re.match("([A-Z]{2}-[0-9]{2}-[A-Z]{2}-[0-9]{4})$", s):
            for cars in plot:  # Function implemented for parking the car.
                if cars == None:  # Extract the licence plate number and check
                    continue  # If duplicate exsits, return null value
                if (
                    cars["licence_plate_no"] == s
                ):  # Extract age and check if it is legal driving age
                    print(
                        "Same car number..bad input"
                    )  # If all constraints check out, perform the function
                    return 0
            parking["licence_plate_no"] = s
        if s.isdigit():
            if int(s) < 18:
                print("Illegal Driving age... not allowed to park")
                return None
            parking["age"] = s
    if parking["licence_plate_no"] == "" or parking["age"] == "":
        return None
    print(
        "Car with vehicle registration number ",
        parking["licence_plate_no"],
        " has been parked at slot number",
        c + 1,
    )
    return parking


def find_car_with_licence_plate(lplate):

    parked_slot = 0
    for (
        cars
    ) in (
        plot
    ):  # Extracting the slot number for the car parked with the given licence plate number
        if cars == None:
            continue
        if cars["licence_plate_no"] == lplate:
            parked_slot = plot.index(cars) + 1
    if parked_slot == 0:
        print("No matching cars found")
        return None
    return parked_slot


def find_cars_with_age(age):
    list_of_slot = []
    for cars in plot:  # Finding slot number of cars of people with same age
        if cars == None:
            continue
        if cars["age"] == age:
            list_of_slot.append(plot.index(cars) + 1)
    if list_of_slot == []:
        print("No matching cars found")
        return None
    return list_of_slot


def get_lic_no_same_age(a):  # Finding licence number of cars with same age
    list_of_cars = []
    for cars in plot:
        if cars == None:
            continue
        if cars["age"] == a:
            list_of_cars.append(cars["licence_plate_no"])
    if list_of_cars == []:
        print("No matching cars found")
        return None
    return list_of_cars


def get_lic_no_slot(slot):
    car_lic_no = None
    for cars in plot:
        if cars == None:
            continue
        if plot.index(cars) == slot:
            car_lic_no = cars["licence_plate_no"]
    if car_lic_no == None:
        print("No matching cars found")
        return None
    return car_lic_no


def min_pos_empty():  # Finding the most closest minimun parking slot which is empty
    empty_slots = []
    for cars in plot:
        if cars == None:
            empty_slots.append(plot.index(cars))
    return empty_slots[0]


n = 0  # size of parking lot
c = 0  # count for iterating in the parking lot
plot = []

filename = input("Enter name of file \n")  # Reading the command file
with open(filename, "r") as f:
    x = f.readline()  # x is the first line of the file
    if (
        x.split()[0].lower() != "create_parking_lot"
    ):  # Creating the database. If the first line is not initializing the database then a message prompt is sent

        print("Please create a database")
        sys.exit()
    else:
        n = [int(i) for i in x.split() if i.isdigit()][0]
        plot = [None] * n
        print("Created parking of ", n, " slots")
    for y in f:  # Reading the other lines of the command file
        full = 0
        if (
            y.split()[0].lower() == "park"
        ):  # Checking if the command is for Parking the car  and running the corresponding function
            while (
                plot[c] != None
            ):  # Park the car if the slot is empty otherwise move to next slot
                c += 1
                if c >= n:
                    print("Parking is full..sorry for the inconvenience")
                    full = 1
                    break
                # print("Checking if car not parked",c)
            if full == 0:
                car_parked = car_park(y)
                if car_parked == None:
                    print("Invalid licence plate number")
                elif car_parked == 0:
                    plot[c] = None
                else:
                    plot[c] = car_parked
            else:
                c = 0
        if (
            y.split()[0].lower() == "leave"
        ):  # Checking if the command is for a car leaving the parking lot
            # print("Removing Car")
            for s in y.split():
                if s.isdigit():  # Extracting the slot number
                    s = int(s)
                    if plot[s - 1] == None:
                        print(
                            "Slot already vacant at", s
                        )  # If the input slot is already vacant
                    elif s - 1 >= n:
                        print(
                            "Please enter a valid slot number"
                        )  # If the slot number is greater than the length of the parking spot
                    else:

                        print(
                            "Slot number",
                            s,
                            " vacated, the car with vehicle registration number ",
                            plot[s - 1]["licence_plate_no"],
                            " left the space, the driver of the car was of age",
                            plot[s - 1]["age"],
                        )
                        plot[s - 1] = None
                        c = (
                            min_pos_empty()
                        )  # vacate the car and bring the count to the nearest parking spot
        if re.match(
            "^Slot_number", y.split()[0]
        ):  # Checking if the command requries to return slot numbers
            nslot = None
            nslots = None
            for s in y.split():
                if re.match(
                    "[A-Z]{2}-[0-9]{2}-[A-Z]{2}-[0-9]{1,4}", s
                ):  # Extracting number plate no to search for the corresponding slot
                    nslot = find_car_with_licence_plate(s)
                if s.isdigit():  # Extracting age to search for the corresponding slot
                    nslots = find_cars_with_age(s)
            if nslot != None:
                print(nslot)
            if nslots != None:
                print(*nslots, sep=",")
        if re.match(
            "^Vehicle_registration_number_for_driver_of_age$ ", y.split()[0]
        ):  # Command to extract the number plate numbers for drivers of same age  or for a given slot number
            lic_nos = None
            for s in y.split():
                if s.isdigit():
                    lic_nos = get_lic_no_same_age(s)
            if lic_nos != None:
                print(*lic_nos, sep=",")
        if re.match(
            "^Vehicle_registration_number_for_parking_slot$", y.split()[0]
        ):  # Command to extract the number plate numbers for drivers of same age  or for a given slot number
            lic_no = None
            for s in y.split():
                if s.isdigit():
                    lic_no = get_lic_no_slot(int(s) - 1)
            if lic_no != None:
                print("The licence plate number of car in slot", s, "is", lic_no)
# print(plot)

    for y in f:                                                      #Reading the other lines of the command file
        full=0  
        if y.split()[0].lower()=="park":                             #Checking if the command is for Parking the car  and running the corresponding function
            while(plot[c]!=None):                                    #Park the car if the slot is empty otherwise move to next slot
                c+=1
                if(c>=n):
                    print("Parking is full..sorry for the inconvenience")
                    full=1
                    break
                #print("Checking if car not parked",c)
            if(full==0):
                car_parked=car_park(y)
                if(car_parked==None):
                    print("Invalid licence plate number")
                elif(car_parked==0):
                    plot[c]=None
                else:
                    plot[c]=car_parked
            else:c=0

        if y.split()[0].lower()=="leave":                                #Checking if the command is for a car leaving the parking lot
            #print("Removing Car")
            for s in y.split():
                if(s.isdigit()):                                         #Extracting the slot number
                    s=int(s)
                    if(plot[s-1]==None):
                        print("Slot already vacant at", s)                #If the input slot is already vacant
                    elif(s-1>=n):
                        print("Please enter a valid slot number")         #If the slot number is greater than the length of the parking spot
                    else:
                        
                        print("Slot number",s," vacated, the car with vehicle registration number ",plot[s-1]["licence_plate_no"]," left the space, the driver of the car was of age", plot[s-1]["age"])
                        plot[s-1]=None
                        c=min_pos_empty()                             #vacate the car and bring the count to the nearest parking spot


        if re.match('^Slot_number',y.split()[0]):                       #Checking if the command requries to return slot numbers
            nslot=None
            nslots=None                                                      
            for s in y.split():
                if(re.match('[A-Z]{2}-[0-9]{2}-[A-Z]{2}-[0-9]{1,4}',s)):             #Extracting number plate no to search for the corresponding slot
                    nslot=find_car_with_licence_plate(s)
                if(s.isdigit()):                                                           #Extracting age to search for the corresponding slot  
                    nslots=find_cars_with_age(s)
            if(nslot!=None):print(nslot)
            if(nslots!=None): print(*nslots,sep=',')

            
        if re.match('^Vehicle_registration_number_for_driver_of_age$ ',y.split()[0]):                                    #Command to extract the number plate numbers for drivers of same age  or for a given slot number                   
            lic_nos=None
            for s in y.split():
                if(s.isdigit()):                     
                    lic_nos=get_lic_no_same_age(s)              
                   
            if(lic_nos!=None):print(*lic_nos,sep=',')
            

        if re.match('^Vehicle_registration_number_for_parking_slot$',y.split()[0]):                                    #Command to extract the number plate numbers for drivers of same age  or for a given slot number                   
            lic_no=None
            for s in y.split():
                if(s.isdigit()):
                    lic_no=get_lic_no_slot(int(s)-1)
            if(lic_no!=None):print("The licence plate number of car in slot",s,"is",lic_no)    

#print(plot)    
