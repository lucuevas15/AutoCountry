##This application will allow users to find a list of 
##vehicles for sale within AutoCountry

#Here is the list input for allowed vehicles

allowedVehicleList = ('Ford F-150', 'Chevrolet Silverado', 'Tesla Cybertruck', 'Toyota Tundra', 'Nissan Titan')

##I created a prompt to make the loop easier##
prompt = "******************************** \nAutoCountry Vehicle Finder v0.1 \n******************************** \nPlease Enter the following number below from the following menu: \n1. PRINT all Authorized Vehicles \n2. Exit"

print (prompt)
answer = input ("select: ")

##While statement for user selections
while answer == '1':
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: \nFord F-150"
"\nChevrolet Silverado \nTesla CyberTruck \nToyota Tundra \nNissan Titan")
    print (prompt)
    answer = input ("select: ")
else:
    print ("Thank you for using the AutoCountry Vehicle Finder, good-bye!")