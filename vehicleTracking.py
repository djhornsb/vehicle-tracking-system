#! python3
# vehicleTracking.py - Super simple initial version of a vehicle tracking system.

import os, sys, meta


## Prints the available options within the system and returns the chosen value

def printOptions():
    maxOptions = 7
    while True:
        print('''Please choose from the following options (enter choice number):

        1. Display a detailed table of the current vehicles
        2. Edit a vehicle's information
        3. Update a vehicle's service information
        4. Display a detailed service history for a vehicle
        5. Add or remove a vehicle from the system
        6. List the vehicles currently in need of servicing
        7. Exit''')
        try:
            choice = int(input())
        except ValueError:
            print('Invalid entry. Please try again.')
            continue
        if choice > 0 and choice <= maxOptions:
            return choice
        else:
            print('Your entry must be between 1 and ' + str(maxOptions))

def main():
    print('Welcome to ' + meta.TITLE + ' Ver ' + meta.VERSION)
    print('By ' + meta.AUTHOR)

    while True:
        opt = printOptions()        
        if opt == 1:
            fullVehicleSummary()    #TODO
        elif opt == 2:
            quickVehicleSummary()   #TODO
            editVehicle()           #TODO
        elif opt == 3:
            quickVehicleSummary()
            serviceVehicle()        #TODO
        elif opt == 4:
            quickVehicleSummary()
            serviceHistory()        #TODO
        elif opt == 5:
            quickVehicleSummary()
            removeVehicle()         #TODO
        elif opt == 6:
            displayNeedService()    #TODO
        else:
            break

    print('Thank you for using ' + meta.TITLE)



main()
