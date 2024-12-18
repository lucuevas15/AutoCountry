##This application will allow users to find a list of 
##vehicles for sale within AutoCountry

#Here is the list input for allowed vehicles
allowedVehicleList =  ['Ford F-150' , 'Chevrolet Silverado' , 'Tesla Cybertruck' , 'Toyota Tundra' , 'Nissan Titan']


##Created a prompt to make the loop easier##
prompt = ("******************************** \nAutoCountry Vehicle Finder v0.4 \n********************************" 
          "\nPlease Enter the following number below from the following menu: \n1. PRINT all Authorized Vehicles "
          "\n2. SEARCH all Authorized Vehicles \n3. ADD Authorized Vehicle \n4. Delete Authorized Vehicle \n5. Exit")

##While statement for loop
while True:
    print(prompt)
    answer = input("select: ")

##If statement for user selections within loop

##Print vehicle list
    if answer == '1':
     print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
     for vehicle in allowedVehicleList:
         print(f"- {vehicle}")
    

##Search for a vehicle
    elif answer == '2':
        print("******************************** \nPLEASE ENTER THE FULL VEHICLE NAME ")
        searchVehicle = input("")
        if searchVehicle in allowedVehicleList:
            print (searchVehicle + " is an authorized vehicle")
        else:
            print (searchVehicle + " is not an authorized vehicle, if you received this in error please check the spelling and try again")

##Add a vehicle to the list
    elif answer == '3':
        print("******************************** \nPlease Enter the full Vehicle name you would like to ADD: ")
        newVehicle = input("")
        if newVehicle not in allowedVehicleList:
            allowedVehicleList.append(newVehicle)
            print(f"You have added {newVehicle} the authorized vehicle list.")
        else:
            print(f"{newVehicle} is already in the authorized vehicle list.")

##Remove a vehicle from the list
    elif answer == '4':
        print("******************************** \nPlease Enter the full Vehicle name you would like to REMOVE: ")
        outdatedVehicle = input("")
        if outdatedVehicle in allowedVehicleList:
            print(f"Are you sure you want to remove {outdatedVehicle} from the Authorized Vehicles List?")
            removeConfirm = input("")
            if removeConfirm == 'yes':
                allowedVehicleList.remove(outdatedVehicle)
                print(f"You have removed {outdatedVehicle} as an authorized vehicle list.")
            else:
                print("The vehicle was not removed")
        else:
            print(f"{newVehicle} is not in the authorized vehicle list.")

#End application
    elif answer == '5':
        print ("******************************** \nThank you for using the AutoCountry Vehicle Finder, good-bye!")
        break

